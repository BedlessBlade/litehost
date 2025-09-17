import socket
from constants import *
import os
import json

def send_command(command):
    with socket.socket() as s:
        s.connect((SERVER_HOST, SERVER_PORT))
        s.sendall(command.encode())
        response = s.recv(1024)
        print("Server response:", response.decode())

def retrieve_json():
    if not os.path.exists(json_name):
        with open(json_name, 'w') as f:
            json.dump({}, f)
        return {}
    try:
        with open(json_name, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading {json_name}: {e}")
        return {}