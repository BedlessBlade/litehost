import socket
from constants import *
from util import *
import threading

#message format to nodes: [command, index]
def construct_command(data):
    command = data[0]
    if data[1]: 
        index = f" {data[1]}"
    else:
        index = ""
    commands = retrieve_json()
    if data in commands:
        return commands[data] + index
    else:
        print(f"No matching command found for {data[0]}")
        return None

def send_command(data, node = DEFAULT_NODE):
    command = construct_command(data)
    if node is not None:
        command = f"{command}"
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(SERVER_TIMEOUT)
            s.connect((NODE_HOST, NODES["CT0"]))
            s.sendall(command.encode())
            try:
                response = s.recv(1024)
            except socket.timeout:
                print("No response received (timeout).")
            print(response.decode())
    else:
        print("Node not specified for command.")

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
                command = data.decode()
                print(f"Received from web: {command}")
                send_command(command)
                conn.sendall(b'ack')

if __name__ == "__main__":
    threading.Thread(target=web_listener, daemon=True).start()