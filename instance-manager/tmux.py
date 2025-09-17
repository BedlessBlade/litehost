import subprocess
from constants import *

def start_server(index):
    name = f"{dirname}{index}"
    try:
        subprocess.run(["tmux", "new-session", "-d", "-s", name, base_path + name + "/pumpkin"], check=True)
    except Exception as e:
        print(f"Error starting server {name}: {e}")

def stop_server(index):
    name = f"{dirname}{index}"
    try:
        subprocess.run(["tmux", "send-keys", "-t", f"{name}:0.0", "stop", "ENTER"], check=True)
    except Exception as e:
        print(f"Error stopping server {name}: {e}")

def announce(data, index):
    name = f"{dirname}{index}"
    try:
        subprocess.run(["tmux", "send-keys", "-t", f"{name}:0.0", "say " + data, "ENTER"], check=True)
    except Exception as e:
        print(f"Error announcing to server {name}: {e}")

def announce_all(data, servers):
    for i in servers:
        announce(data, i)

def stop_all(servers):
    for i in servers:
        stop_server(i)

def start_all(servers):
    for i in servers:
        start_server(i)