#!/usr/bin/env python3
import json
import os
from constants import json_name

def save_json(data):
    try:
        with open(json_name, 'w') as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        print(f"Error saving {json_name}: {e}")
        return
    print(f"Commands saved to {json_name}")

def retrieve_json():
    try:
        with open(json_name, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error reading {json_name}: {e}")
        return {}

def remove_command(command):
    data = retrieve_json()
    if not data:
        print("No commands to remove.")
        return
    print("Current commands:")
    for idx, (cmd, action) in enumerate(data.items(), 1):
        print(f"{idx}. {cmd}: {action}")
    if command in data:
        del data[command]
        save_json(data)
        print(f"Command '{command}' removed.")
    else:
        print(f"Command '{command}' not found.")

def add_command(command, action):
    data = retrieve_json()
    data[command] = action
    save_json(data)
    print(f"Command '{command}' added/updated.")

def prompt_user(prompt):
    print(prompt)
    return input("> ").strip()

def startup():
    print("Welcome to the Command Management Utility.")
    print("Please choose an option:")
    print("1. Add/Update Command")
    print("2. Remove Command")
    print("3. Exit")
    return input("> ").strip()

if __name__ == "__main__":
    while True:
        choice = startup()

        if choice == '1':
            cmd = prompt_user("Enter command name:")
            action = prompt_user("Enter command action:")
            add_command(cmd, action)
        elif choice == '2':
            data = retrieve_json()
            if not data:
                print("No commands to remove.")
            else:
                print("Current commands:")
                cmd_list = list(data.keys())
                for idx, (cmd, action) in enumerate(data.items(), 1):
                    print(f"{idx}. {cmd}: {action}")
                user_input = prompt_user("Enter command name or number to remove:")
                to_remove = user_input
                if user_input.isdigit():
                    num = int(user_input)
                    if 1 <= num <= len(cmd_list):
                        to_remove = cmd_list[num - 1]
                    else:
                        print("Invalid number.")
                        to_remove = None
                if to_remove:
                    remove_command(to_remove)
        elif choice == '3':
            print("Exiting.")
            break
        else:
            print("Invalid choice.")
