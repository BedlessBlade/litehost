import socket; from constants import *; from util import *;

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

def send_command(data, node = None):
    command = construct_command(data)
    if node is not None:
        command = f"{command} {node}"

    

if __name__ == "__main__":
