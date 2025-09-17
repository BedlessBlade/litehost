import os
from constants import *
from tmux import stop_server

def create_instance(index):
    name = f"instances/{dirname}{index}"
    try:
        os.makedirs(name, exist_ok=True)
    except Exception as e:
        print(f"Error creating directory {name}: {e}")
    try:
        os.symlink("pumpkin", f"{name}/pumpkin")
    except Exception as e:
        print(f"Error creating symlink in {name}: {e}")

def destroy_instance(index):
    stop_server(index)
    name = f"instances/{dirname}{index}"
    try:
        os.rmdir(name)
    except Exception as e:
        print(f"Error removing directory {name}: {e}")

def pumpkin_update():
    try:
        os.remove("Pumpkin")
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error removing Pumpkin: {e}")
    os.system(f"git clone https://github.com/Pumpkin-MC/Pumpkin.git && cd Pumpkin && RUSTFLAGS='-C target-cpu=native' cargo build --release -j {compiling_threads}")
    os.system("mv ./target/releases/pumpkin .. && cd ..")