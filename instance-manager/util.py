import os; from constants import *; from tmux import stop_server
 
def create_instance(index):
    name = f"instances/{dirname + index}"
    os.system(f'mkdir {name}')
    os.system(f"ln -s pumpkin {name}/pumpkin")

def destroy_instance(index):
    stop_server(index)
    name = f"instances/{dirname + index}"
    os.system(f"rm {name}")

def pumpkin_update():
    os.system(f"rm Pumpkin && git clone https://github.com/Pumpkin-MC/Pumpkin.git && cd Pumpkin && RUSTFLAGS='-C target-cpu=native' cargo build --release -j {compiling_threads}")
    os.system("mv ./target/releases/pumpkin .. && cd ..")