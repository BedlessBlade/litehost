import subprocess; from constants import *

def start_server(index):
    name = dirname + index
    subprocess.run(["tmux", "new-session", "-d", "-s", name, base_path + name])
def stop_server(index):
    name = dirname + index
    subprocess.run(["tmux", "send-keys", "-t", f"{name}:0.0", "stop", "ENTER"])
def announce(data, index):
    name = dirname + index
    subprocess.run(["tmux", "send-keys", "-t", f"{name}:0.0", "say " + data, "ENTER"])
def announce_all(data, servers):
    for i in range(len(servers)):
        announce(data, i)
def stop_all(servers):
    for i in range(len(servers)):
        stop_server(i)
def start_all(servers):
    for i in range(len(servers)):
        start_server(i)