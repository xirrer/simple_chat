from socket import *

client = socket(AF_INET, SOCK_STREAM)
client.connect(("127.0.0.1", 7000))

while True:
    # Добавляем возможность отправки сообщения клиента серверу
    client_msg = input("Client: ")  # Приглашение для ввода сообщения клиента
    client.send(client_msg.encode('utf-8'))  # Отправляем сообщение серверу
    
    received_server_message = client.recv(1024)
    received_server_message = received_server_message.decode('utf-8')
    print("Server:", received_server_message)  # Выводим сообщение от сервера