import time, socket, sys, ssl
 
socket_server = socket.socket()
server_host = socket.gethostname()
ip = socket.gethostbyname(server_host)
sport = 8080
 ccontext = ssl.create_default_context()

print('This is your IP address: ',ip)
server_host = input('Enter friend\'s IP address:')
name = input('Enter Friend\'s name: ')
 
 
socket_server.connect((server_host, sport))
  ssocket_server = ccontext.wrap_socket(socket_server, server_host) 
      
ssocket_server.send(name.encode())
server_name = ssocket_server.recv(1024)
server_name = server_name.decode()
  
print(server_name,' has joined...')
while True:
    message = (ssocket_server.recv(1024)).decode()
    print(server_name, ":", message)
    message = input("Me : ")
    ssocket_server.send(message.encode())