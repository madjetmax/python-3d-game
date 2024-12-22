import socket
import json
from copy import deepcopy
from confin import *



class Server():
    def __init__(self):
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server.bind((HOST, PORT))
        self.server.listen()
        self.players = []

        
        

    def run_connection(self):
        while True:
            conn, addr = self.server.accept()    
            data = conn.recv(1024).decode()



            if data.startswith("plr_join_"):
                plr_name = data.replace("plr_join_", "")
                new_plr = {
                    "name": plr_name,
                    "x": 0, "y": 0, "z": 0
                }

                all_names = [p["name"] for p in self.players]
                if plr_name not in all_names:
                    self.players.append(
                        new_plr
                    )
                    conn.send(json.dumps(new_plr).encode())
                
                print(self.players)
            
            if data.startswith("plr_leave_"):
                plr_name = data.replace("plr_leave_", "")
                
                for plr in self.players:
                    if plr["name"] == plr_name:
                        self.players.remove(plr)
                
                print(self.players)

            if data.startswith("p_pos_"):
                plr_name = data.replace("p_pos_", "").split("_")[0]
                x, y, z = data.replace("p_pos_", "").split("_")[1].split('/')
                for plr in self.players:
                    if plr["name"] == plr_name:
                        plr["x"] = x
                        plr["y"] = y
                        plr["z"] = z
                other_players = [p for p in self.players if p["name"] != plr_name]
                conn.send(json.dumps(other_players).encode())
                # print(x, y, z)


            conn.shutdown(socket.SHUT_WR)
            if data == "close_server":
                break

if __name__ == "__main__":
    server = Server()
    server.run_connection()
