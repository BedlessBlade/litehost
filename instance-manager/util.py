import os; from constants import *

def create_instance(index):
    name = f"instances/{dirname} + {index}"
    os.system(f'mkdir {name}')
    os.chdir(name)

def pumpkin_update():
    os.system(f"rm Pumpkin && git clone https://github.com/Pumpkin-MC/Pumpkin.git && cd Pumpkin && RUSTFLAGS='-C target-cpu=native' cargo build --release -j {compiling_threads}")
    os.system("mv ./target/releases/pumpkin .. && cd ..")