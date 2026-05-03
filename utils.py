import json

def load_data():
    with open("data.json", "r") as file:
        return json.load(file)

def print_steps(steps):
    for i, step in enumerate(steps, 1):
        print(f"{i}. {step}")