import atexit
import socket


class Server(object):

    def __init__(self, host, port):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((host, port))
        atexit.register(self._cleanup)
        
    def start(self):
        self.server.listen(1)
        client_connection, address = self.server.accept()
        while True:
            data = client_connection.recv(1024)
            if data:
                print(data.decode())
            # TODO: detect client disconnect

    def _cleanup(self):
        self.server.close()
