from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(("127.0.0.1", 7000))
server.listen(10)

user, addr = server.accept()
print("Connected")

while True:
    server_msg = input("Server: ")  # Приглашение для ввода сообщения сервера
    user.send(server_msg.encode('utf-8'))  # Отправляем сообщение клиенту
    
    data = user.recv(1024)
    received_message = data.decode("utf-8")
    print("Client:", received_message)  # Выводим сообщение от клиента
    
    # Добавляем возможность отправки сообщения сервера клиенту

