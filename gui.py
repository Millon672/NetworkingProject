import socket
from kivy.app import App
from kivy.uix.button import Button
import select
from threading import Thread

"""
HOST = input('Enter host: ')
PORT = input('Enter port: ')
PORT = int(PORT)
username = input('enter username: ')
username = username.encode("utf-8")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))
server.send(username)
"""
def send(event=None):
    message = client_message.get()
    
    if client_message == 'quit':
        server.close()
        gui.destroy()
        
    chat_log.insert(tkinter.END, "<You>" + message)
    client_message.set("")
    server.send(message.encode("utf-8"))
    
def receive():
    while True:
        try:
            message = server.recv(2048).decode("utf-8")
            chat_log.insert(tkinter.END, message)

        except OSError:
            break;
        
def closeWindow(event=None):
    server.close()
    gui.destroy()

#gui = tkinter.Tk()
#gui.title("PorkChop's Lounge")
class TestApp(App):
    def build(self):
        return Button(text='Hello World')

TestApp().run()

