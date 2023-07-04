from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(("ip", port))
server.listen(10)

user, addr = server.accept()
print("Connected")

while True:
    server_msg = input("Server: ")
    user.send(server_msg.encode('utf-8'))
    
    data = user.recv(1024)
    received_message = data.decode("utf-8")
    print("Client:", received_message)
