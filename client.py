# Python program to implement client side of chat room.
import socket
import select
import sys
import signal


def signal_handle_CTRL_C(signum, frame):
    print ("\nexiting...")
    server.close()
    exit()





server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)



if len(sys.argv) != 4:
    print "Correct usage: script, IP address, port number, username"
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
username = str(sys.argv[3])

server.connect((IP_address, Port))
server.send(username + "\n")  
while True:
  
    # maintains a list of possible input streams
    sockets_list = [sys.stdin, server]
  
    """The user gives  manual input to send to other people,
    or the server is sending a message  to be printed on the
    screen. Select returns from sockets_list, the stream that
    is reader for input."""
    read_sockets,write_socket, error_socket = select.select(sockets_list,[],[])
  
    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)

            # we have an error with sending the message
            # server is down
            if not message:
                print "Server connection error"
                signal_handle_CTRL_C(signal.SIGSTOP,None)
            else:
                print message
        else:
            message = sys.stdin.readline()
            server.send(message)
            sys.stdout.write("<You>")
            sys.stdout.write(message)
            sys.stdout.flush()

    # setting the signal handler for SIGINT ^C
    # view signal_handle_CTRL_C
    sig = signal.signal(signal.SIGINT, signal_handle_CTRL_C)