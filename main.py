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
                """
                data = data.decode("utf-8")
                if data == 'notif':
                    self.label.text = "Server detected coughing in the area..."
                    try:
                        self.notif_handler.notify(title="Alert", message="Someone coughed nearby! Watch out!")
                        vibrator.vibrate(time=1)
                    except:
                        self.label.text = "Erro a mandar notificacao"

                """
            connection.close()
            self.label.text = "Server disconnected"
                


class MyGrid(GridLayout):
    def __init__(self, **kwargs):
        super(MyGrid, self).__init__(**kwargs)

        # Criar UI (1)
        """
        self.rows = 2
        self.state = "stopped"

        self.label = Label(text="Default Text")
        self.add_widget(self.label)

        self.button = Button(text="Record!")
        self.add_widget(self.button)


        self.button.bind(on_press=partial(self.toogle_recording, [self.button, self.label]))
        """

        # Definir o agente de geracao de notificacoes da libray plyer (6)
        """
        self.notif_handler = notification
        """

        # Ativar a thread que fica a escuta por respostas do servidor (8)
        """
        listening_thread = ListeningThread(self.label, self.notif_handler)
        listening_thread.start()
        """
        
    def toogle_recording(self, instance, *args):
        if self.state == "stopped":
            self.button.text = "Stop Recording!"
            self.state = "recording"
            self.button.disabled = True

            # Capturar audio atraves da library plyer (2)
            """
            audio.start()
            """
            # Reativar o botao dentro de 4 segundos (3)
            """
            Clock.schedule_once(self.enable_button, 4)
            """
            
        else:
            self.button.text = "Start Recording!"
            self.state = "stopped"

            # Parar a captura de som (4)
            """
            audio.stop()
            """

            # Conectar ao servidor e enviar o ficheiro de audio para avaliacao (5)
            """
            self.HOST = '192.168.1.88'  # The server's hostname or IP address
            self.PORT = 44433
            self.sending_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.sending_socket.connect((self.HOST, self.PORT))

            file_path = audio.file_path
            with open(file_path, 'rb') as file:
                bytes = file.read(1024)
                while bytes:
                    self.sending_socket.send(bytes)
                    bytes = file.read(1024)
            self.sending_socket.close()
            """
        
        # Reativar o botao dentro de 4 segundos (3)
    """
    def enable_button(self, dt):
        self.button.disabled = False
    """
        

class KivyApp(App):

    def build(self):
        return MyGrid()

KivyApp().run()