#save load
import json

import os


SAVE_DIR = "saves"
os.makedirs(SAVE_DIR, exist_ok=True)

def save_game(data, slot): #saves current status to current save slot, aka currect save file
    filepath = os.path.join(SAVE_DIR, f"save_slot_{slot}.json")
    with open(filepath, "w") as f:
        json.dump(data, f, indent=4)

def load_game(slot):
    filepath = os.path.join(SAVE_DIR, f"save_slot_{slot}.json")
    if not os.path.exists(filepath):
        return None  # No save yet
    with open(filepath, "r") as f:
        return json.load(f)

def delete_save(slot):
    filepath = os.path.join(SAVE_DIR, f"save_slot_{slot}.json")
    if os.path.exists(filepath):
        os.remove(filepath)

def list_saves(slot_count=3):
    status = []
    for slot in range(1, slot_count + 1):
        filepath = os.path.join(SAVE_DIR, f"save_slot_{slot}.json")
        if os.path.exists(filepath):
            with open(filepath) as f:
                data = json.load(f)
                name = data.get("player_name", "Unknown")
                level = data.get("level", "?")
                status.append(f"[{slot}] {name} (Level {level})")
        else:
            status.append(f"[{slot}] Empty")
    return status

