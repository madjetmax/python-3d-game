import socket


HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)



def main():
    try:
        server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server.bind((HOST, PORT))
        server.listen(4)
        while True:
            print("WAIT")
            conn, addr = server.accept()    
            data = conn.recv(1024)
            conn.send("hello".encode())

            conn.shutdown(socket.SHUT_RD)
            if data.decode() == "c":
                break
    except KeyboardInterrupt:
        server.close()




if __name__ == "__main__":
    main()

