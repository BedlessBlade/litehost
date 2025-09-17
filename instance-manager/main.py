import socket, os; from constants import *; from tmux import *; from util import *

try:
    os.system(f'ssh -L {server_port}:127.0.0.1:{ssh_port} {ssh_user}@{ssh_hostname}')
except Exception as e:
    print("SSH Tunnel Error: " + str(e))
server = socket.socket()
try:
    server.bind((ssh_hostname, server_port))
except Exception as e:
    print("Socket Bind Error: " + str(e))
server.listen()

conn, addr = server.accept()


while True:
    data = conn.recv(1024)
    if not data:
        break
    args = data.decode().split(" ")
    if len(args) > 0:
        if data.decode()[0] == 'start':
            start_server(args[1])
        elif data.decode()[0] == 'stop':
            stop_server(args[1])
        elif data.decode()[0] == 'announce':
            #todo: fix announce
            pass
        elif data.decode()[0] == 'create':
            create_instance(args[1])
        elif data.decode()[0] == 'destroy':
            destroy_instance(args[1])
        elif data.decode()[0] == 'update':
            pumpkin_update()
        elif data.decode()[0] == 'startall':
            start_all(args[1])
        elif data.decode()[0] == 'stopall':
            stop_all(args[1])
    conn.send(b'ack')

conn.close()
server.close()
        
            

