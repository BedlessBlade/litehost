import socket, os; from constants import *

os.system(f'ssh -L {server_port}:127.0.0.1:{ssh_port} {ssh_user}@{ssh_hostname}')

server = socket.socket()
server.bind((ssh_hostname, server_port))
server.listen()

conn, addr = server.accept()


while True:
    data = conn.recv(1024)
    if not data:
        break
    if data.decode() == "":
        #placeholder
        