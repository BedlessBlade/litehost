import subprocess; from constants import *

def make_session(index):
    name = dirname + index
    subprocess.run(["tmux", "new-session", "-d", "-s", name, base_path + name])

def stop_server(index):
    name = dirname + index
    subprocess.run(["tmux", "send-keys", "-t", f"{name}:0.0", "stop", "ENTER"])

def announce(data, index):
    name = dirname + index
    subprocess.run(["tmux", "send-keys", "-t", f"{name}:0.0", "say " + data, "ENTER"])
