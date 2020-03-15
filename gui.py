import tkinter
import socket
import select
from threading import Thread

HOST = input('Enter host: ')
PORT = input('Enter port: ')
PORT = int(PORT)
username = input('enter username: ')
username = username.encode("utf-8")
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.connect((HOST, PORT))
server.send(username)

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

gui = tkinter.Tk()
gui.title("PorkChop's Lounge")

messages_frame = tkinter.Frame(gui)
client_message = tkinter.StringVar()  # For the messages to be sent.
client_message.set("Type your messages here.")
scrollbar = tkinter.Scrollbar(messages_frame)  # To navigate through past messages.
# Following will contain the messages.
chat_log = tkinter.Listbox(messages_frame, height=15, width=50, yscrollcommand=scrollbar.set)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
chat_log.pack(side=tkinter.LEFT, fill=tkinter.BOTH)
chat_log.pack()
messages_frame.pack()
#this is the box you actually enter text into
entry_field = tkinter.Entry(gui, textvariable=client_message)
#trying to fix the enter key but not working
entry_field.bind("<Return>", send)
entry_field.pack()
#send button
send_button = tkinter.Button(gui, text="Send", command=send)
send_button.pack()
#signal handler for if the user clicks off the window
gui.protocol("WM_DELETE_WINDOW", closeWindow)

receive_thread = Thread(target=receive)
receive_thread.start()
tkinter.mainloop()
