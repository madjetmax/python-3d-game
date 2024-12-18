import socket
import json



HOST = "127.0.0.1"
PORT = 65432  

class Client():
    def __init__(self):
        self.plr_name = "tolik"

    def send_plr_join(self):
        self.server = socket.socket()
        self.server.connect((HOST, PORT))
        self.server.send(f"plr_join_{self.plr_name}".encode())
        server_data = self.server.recv(1024).decode()
        print(server_data)
        # if data.startswith("plr_join"):
        self.server.close()

    def send_pos(self, x, y, z):
        self.server = socket.socket()
        self.server.connect((HOST, PORT))
        self.server.send(f"p_pos_{self.plr_name}_{int(x)}/{int(y)}/{int(z)}".encode())
        server_data = self.server.recv(1024).decode()

        # print(json.loads(server_data))
        # if data.startswith("plr_join"):
        self.server.close()


    def send_data(self, data: str):
        self.server = socket.socket()
        self.server.connect(('127.0.0.1', 65432))
        self.server.send(data.encode())
        
        server_data = self.server.recv(1024).decode()
        print(server_data)
        # if data.startswith("plr_join"):
            
        self.server.close()
        


client = Client()