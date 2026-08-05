import json
import os

def read_data(file_name):
    # Mencari path ke direktori root project
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', file_name)
    
    with open(file_path, 'r') as file:
        return json.load(file)
