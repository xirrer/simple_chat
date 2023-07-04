from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(("ip", port))

while True:
    client_msg = input("Client: ") 
    client.send(client_msg.encode('utf-8'))
    
    received_server_message = client.recv(1024)
    received_server_message = received_server_message.decode('utf-8')
    print("Server:", received_server_message)
