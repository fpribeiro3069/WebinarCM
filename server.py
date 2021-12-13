import socket
from _thread import *

import queue
import os, sys, signal
import datetime

import librosa
from keras.models import load_model
import numpy as np

from time import sleep

HOST = '0.0.0.0'
PORT = 44433

sending_sock_list = []

q = queue.Queue()

def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("Binding to " + HOST)
    try:
        server_socket.bind((HOST, PORT))
    except socket.error as e:
        print(str(e) + " Please restart the server!")
        sys.exit(0)

    # Carregar o modelo de Inteligência Artificial (1)




    print('Waiting for a Connection..')
    server_socket.listen(5)

    while True:
        connection, address = server_socket.accept()
        print('Connected to: ' + address[0] + ':' + str(address[1]))

        # Cria thread para lidar com a nova conexão
        start_new_thread(threaded_client, (connection, address, model))
        # Quando um cliente se liga ao servidor, o servidor liga-se
        # também ao socket do cliente da escuta de mensagens 
        identifier = start_new_thread(sending_thread, (address, ))

        sending_sock_list.append(identifier)


def threaded_client(connection, address, model):

    # Receber o ficheiro de audio que o cliente quer mandar
    with open('audio_file.3gp', 'wb') as file:
        bytes = connection.recv(1024)
        while bytes:
            file.write(bytes)
            bytes = connection.recv(1024)
        
    if not os.path.exists('wav_folder'):
        os.makedirs('wav_folder') 

    nowTime = datetime.datetime.now().strftime('%m-%d-%H-%M-%S')
    filename = 'wav_folder/audio_file_' + str(nowTime) + '.wav'
    # Transformar o ficheiro 3gp em wav para ser aceite pelo modelo (2)
    




    # Avaliar por IA se o som recebido é de facto uma tosse através da 
    # função getCoughProbability() (3)





    # Definir o limite aceitável de probabilidade de tosse e enviar
    # mensagem para todos os clientes ligados se for tosse (4)





def sending_thread(address):
    sending_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sending_socket.connect((address[0], 44434))
    except socket.error as e:
        print("Trouble connecting to client socket for responses -> " + str(e))
        sending_socket.close()
        return

    # Enviar mensagem para todos os clientes ligados ao servidor
    # com exceção do cliente que enviou o audio (5)
   






def getCoughProbability(filename, model):
    # Conjunto de passos para preparar o ficheiro para a predição no
    # modelo. Este modelo requer que os ficheiros tenham cerca de 3
    # segundos de duração.
    y , sr = librosa.load(filename, duration=2.97)
    mel_spect = librosa.feature.melspectrogram(y=y, sr=sr)
    mel_spect.resize(128,128,refcheck=False)
    mel_spect = np.array(mel_spect.reshape((1,128,128,1)))
    mel_spect = np.array(mel_spect)
    # Avaliar
    predicted = model.predict(mel_spect)
    cough_percentage = predicted[0][0] * 100

    return cough_percentage

if __name__ == '__main__':
    main()