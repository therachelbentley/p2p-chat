import atexit
import errno
import fileinput
import socket
import time


class Client(object):

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def start(self): 
        while True:
            try:
                self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self.client.connect((self.host, self.port))
                atexit.register(self._cleanup)
                break
            except socket.error as err:
                if err.errno != errno.ECONNREFUSED:
                    raise err
                print("Could not connect to peer. Trying again in 5 seconds.")
                time.sleep(5)
        print("Connection established with peer.")
        while True:
            msg = fileinput.input()
            for line in msg:
                self.client.sendall(line.encode())
        


    def _cleanup(self):
        self.client.close()
