import socket
from constants import *
from util import *
import threading

# message format to nodes: [command, index]
def construct_command(data):
    command = data[0]
    if len(data) > 1 and data[1]:
        index = f" {data[1]}"
    else:
        index = ""
    commands = retrieve_json()
    if command in commands:
        return commands[command] + index
    else:
        print(f"No matching command found for {command}")
        return None

def send_command(data, node=DEFAULT_NODE):
    if isinstance(data, str):
        data = data.strip().split()
    command = construct_command(data)
    if command is None:
        print("No command to send.")
        return
    if node is not None:
        if node in NODES:
            # NOTE: send_command does NOT open a connection anymore
            print(f"send_command is now expected to use an open connection for node '{node}'.")
            # You can implement persistent connection usage here later.
        else:
            print(f"Node '{node}' not found in NODES.")
    else:
        print("Node not specified for command.")

def handle_command(command):
    # You can expand this to actually process commands and return responses
    # For now, just print and return a generic ACK
    print(f"Handling command: {command}")
    return 'ACK'

def node_server():
    node = "CT0"
    if node in NODES:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            server_socket.bind((NODE_HOST, NODES[node]))
            server_socket.listen(1)  # Listen for 1 connection at a time
            print(f"Node Manager listening for node '{node}' on {NODE_HOST}:{NODES[node]}")
            while True:
                print("Waiting for a connection...")
                conn, addr = server_socket.accept()
                print(f"Connected by {addr}")
                with conn:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            print(f"Connection closed by {addr}")
                            break
                        command = data.decode().strip().split()
                        print(f"Received command: {command}")
                        response = handle_command(command)
                        conn.sendall(response.encode() if response else b'ACK')
    else:
        print(f"Node '{node}' not found in NODES.")

def web_listener():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((WEB_IP, WEB_PORT))
        s.listen()
        print(f"Listening for web integration on {WEB_IP}:{WEB_PORT}")
        while True:
            conn, addr = s.accept()
            with conn:
                data = conn.recv(1024)
                if not data:
                    continue
                command = data.decode().strip().split()
                print(f"Received from web: {command}")
                send_command(command)
                conn.sendall(b'ack')

if __name__ == "__main__":
    threading.Thread(target=node_server, daemon=True).start()
    # threading.Thread(target=web_listener, daemon=True).start()
    user_input = input("bro it works lets fucking go\n")
    send_command(user_input)
