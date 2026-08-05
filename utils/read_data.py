from pathlib import Path
import json

DATA_DIR = Path(__file__).parent.parent / "data"

def read_data(file_name: str):
    with open(DATA_DIR / file_name, encoding="utf-8") as f:
        return json.load(f)