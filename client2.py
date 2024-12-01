import socket
client_socket=socket.socket()
client_socket.connect(('localhost',1234))
print("connected")
file=input("enter the filename")
with open(file,'wb') as file:
    while True:
        data=client_socket.recv(1024)
        if not data:
            break
        file.write(data)
    
client_socket.close()
    
