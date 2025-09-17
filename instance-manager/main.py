online_instances = set()
import socket, os
from constants import *
from tmux import *
from util import *

def safe_int(val):
    try:
        return int(val)
    except Exception:
        return None

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

conn = None
try:
    conn, addr = server.accept()
    online_instances = set()
    while True:
        try:
            data = conn.recv(1024)
            if not data:
                break
            args = data.decode().strip().split(" ")
            if not args or not args[0]:
                continue
            cmd = args[0]
            if cmd == 'start' and len(args) > 1:
                idx = safe_int(args[1])
                if idx is not None:
                    try:
                        start_server(idx)
                        online_instances.add(idx)
                    except Exception as e:
                        print(f"Error starting server {idx}: {e}")
            elif cmd == 'stop' and len(args) > 1:
                idx = safe_int(args[1])
                if idx is not None:
                    try:
                        stop_server(idx)
                        online_instances.discard(idx)
                    except Exception as e:
                        print(f"Error stopping server {idx}: {e}")
            elif cmd == 'announce' and len(args) > 2:
                idx = safe_int(args[1])
                message = ' '.join(args[2:])
                if idx is not None and idx in online_instances:
                    try:
                        announce(message, idx)
                    except Exception as e:
                        print(f"Error announcing to server {idx}: {e}")
            elif cmd == 'announceall' and len(args) > 1:
                message = ' '.join(args[1:])
                for idx in online_instances:
                    try:
                        announce(message, idx)
                    except Exception as e:
                        print(f"Error announcing to server {idx}: {e}")
            elif cmd == 'create' and len(args) > 1:
                try:
                    create_instance(args[1])
                except Exception as e:
                    print(f"Error creating instance {args[1]}: {e}")
            elif cmd == 'destroy' and len(args) > 1:
                try:
                    destroy_instance(args[1])
                except Exception as e:
                    print(f"Error destroying instance {args[1]}: {e}")
            elif cmd == 'update':
                try:
                    pumpkin_update()
                except Exception as e:
                    print(f"Error updating pumpkin: {e}")
            elif cmd == 'startall' and len(args) > 1:
                try:
                    start_all(args[1])
                except Exception as e:
                    print(f"Error starting all: {e}")
            elif cmd == 'stopall' and len(args) > 1:
                try:
                    stop_all(args[1])
                except Exception as e:
                    print(f"Error stopping all: {e}")
            conn.send(b'ack')
        except Exception as e:
            print(f"Error in main loop: {e}")
            try:
                conn.send(b'nack')
            except Exception:
                pass
            continue
finally:
    if conn:
        conn.close()
    server.close()



