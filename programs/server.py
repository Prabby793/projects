import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = "localhost"
port = 12345
#bindingsocket
s.bind((host,port))
#listeningforclients
s.listen(5)
print("socket is listening.")
#accepting connections
conn, addr = s.accept()
print("Got connection from", addr)
while True:
    data = input("server: ")
    conn.sendall(data.encode())
    message = conn.recv(50)
    print(addr,message.decode())
