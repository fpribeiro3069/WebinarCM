from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.app import App
from kivy.clock import Clock
from functools import partial

# Audio & Notification imports
from plyer import audio, notification, vibrator

import socket, threading

class ListeningThread(threading.Thread):
    def __init__(self, label, notif_handler):
        threading.Thread.__init__(self)
        self.PORT = 44434
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.label = label
        self.notif_handler = notif_handler

    def run(self):
        self.server_socket.bind(('0.0.0.0', self.PORT))
        self.server_socket.listen(1)

        while True:
            connection, address = self.server_socket.accept()
            self.label.text = "Server is connected to my listening thread"

            while True:
                data = connection.recv(1024)
                if not data:
                    break
                
                # Receber a mensagem do servidor e transmitir ao user a notificacao (7)
                


                
            connection.close()
            self.label.text = "Server disconnected"
                


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        # Criar UI (1)
        





        # Definir o agente de geracao de notificacoes da libray plyer (6)
        


        # Ativar a thread que fica a escuta por respostas do servidor (8)
        
        
    def toogle_recording(self, instance, *args):
        if self.state == "stopped":
            self.button.text = "Stop Recording!"
            self.state = "recording"
            self.button.disabled = True

            # Capturar audio atraves da library plyer (2)
            
            # Reativar o botao dentro de 4 segundos (3)
            
            
        else:
            self.button.text = "Start Recording!"
            self.state = "stopped"

            # Parar a captura de som (4)
            

            # Conectar ao servidor e enviar o ficheiro de audio para avaliacao (5)
            

        
    # Reativar o botao dentro de 4 segundos (3)
    
        

class KivyApp(App):

    def build(self):
        return MyGrid()

KivyApp().run()