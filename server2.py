import socket
server_socket=socket.socket()
server_socket.bind(('localhost',1234))
server_socket.listen(1)
print("server is connceting..")
client_socket,client_addr=server_socket.accept()

with open('ex.txt','rb')as file:
    file_data=file.read(1024)
    while file_data:
        client_socket.send(file_data)
        file_data=file.read(1024)
    
server_socket.close()
client_socket.close()