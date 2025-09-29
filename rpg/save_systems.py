import json
import os
from datetime import date
from .player import Player

SLOTS_FILE = "data/saves/slots.json"

def init_slots(num_slots = 3):
    os.makedirs("data/saves", exist_ok = True)

    if not os.path.exists(SLOTS_FILE):
        slots = []
        for i in range(1, num_slots + 1):
            slots.append({
                "id": i,
                "name": None,
                "level": None,
                "last_played": None,
                "file": f"data/saves/slot{i}.json",
            })
        with open(SLOTS_FILE, "w") as f:
            json.dump({"slots": slots}, f, indent=4)

def update_slots(player, slot_id):
    slot_id = int(slot_id)
    with open(SLOTS_FILE, "r") as f:
        slots_data = json.load(f)

    for slot in slots_data["slots"]:
        if slot["id"] == slot_id:
            slot["name"] = player.name
            slot["level"] = player.level
            slot["last_played"] = str(date.today())
            break

    with open(SLOTS_FILE, "w") as f:
        json.dump(slots_data, f, indent=4)

def delete_slot(slot_id):
    slot_id = int(slot_id)
    slot_file = f"data/saves/slot{slot_id}.json"
    if os.path.exists(slot_file):
        os.remove(slot_file)
        print(f"Deleted {slot_file}")
    else:
        print("Slot file does not exist")

    with open(SLOTS_FILE, "r") as f:
        slots_data = json.load(f)

    for slot in slots_data["slots"]:
        if slot["id"] == slot_id:
            slot["name"] = None
            slot["level"] = None
            slot["last_played"] = None
            break

    with open(SLOTS_FILE, "w") as f:
        json.dump(slots_data, f, indent=4)

class SaveManager:
    def __init__(self, folder="data/saves"):
        self.folder = folder

    def save_game(self, player, slot_id):
        player_data = player.to_dict()
        with open(f"{self.folder}/slot{slot_id}.json", "w") as f:
            json.dump(player_data, f, indent=4)
        update_slots(player, slot_id)

    def load_game(self, slot_id):
        if os.path.exists(f"{self.folder}/slot{slot_id}.json"):
            slot_id = int(slot_id)
            with open(f"{self.folder}/slot{slot_id}.json", "r") as f:
                player_data = json.load(f)

            return Player.from_dict(player_data)
        return None

    def display_slots(self):
        with open(SLOTS_FILE, "r") as f:
            data = json.load(f)
        print("Available save slots:")
        for slot in data["slots"]:
            if slot["name"]:
                print(f'{slot["id"]}. {slot["name"]} (Level {slot["level"]})')
            else:
                print(f'{slot["id"]}. Empty')

    def choose_save_slot(self):
        while True:
            self.display_slots()
            slots_choice = input("Choose a save slot (choose an empty slot to create a new save and type 'd' to delete a save) > ").strip()
            if slots_choice == 'd':
                slot_to_delete = int(input("Choose a save slot to delete > "))
                confirmation_prompt = input("Are you ABSOLUTELY sure you want to PERMANENTLY delete this save? (y/n) > ").lower()
                if confirmation_prompt == 'y':
                    delete_slot(slot_to_delete)
                else:
                    print("Canceling Slot Deletion...")
            elif slots_choice == '1' or slots_choice == '2' or slots_choice == '3':
                return slots_choice
        return slots_choice