import atexit
import threading
from client import Client
from server import Server

class ChatApp(object):
    """ Chat application instance.
    """

    def __init__(self, server_host, server_port, client_host, client_port):
        server = Server(server_host, server_port)
        client = Client(client_host, client_port) 

        threading.Thread(target=server.start, name="Thread-Server").start()
        threading.Thread(target=client.start, name="Thread-Client").start() 
