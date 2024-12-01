import socket
client_socket=socket.socket()
client_socket.connect(('localhost',1234))
print("connected")
while True:
    msg=input("enter a message")
    if msg=="bye":
        print("disconnevted")
        break
    client_socket.send(msg.encode())

    server_msg=client_socket.recv(1024).decode()
    if server_msg=="bye":
        print("disconnected")
        break
    print("server",server_msg)
client_socket.close()
    
