import socket
server_socket=socket.socket()
server_socket.bind(('localhost',1234))
server_socket.listen(1)
print("server is connceting..")
client_socket,client_addr=server_socket.accept()

while True:
    msg=client_socket.recv(1024).decode()
    if msg=='bye':
        print("disconnected")
        break
    print("client",msg)

    server_msg=input("you:")
    client_socket.send(server_msg.encode())

    if server_msg=='bye':
        print("disconnected")
        break
server_socket.close()
client_socket.close()