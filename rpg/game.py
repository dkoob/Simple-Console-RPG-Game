from .player import Player
from .save_systems import SaveManager
from .utils import display_settings, display_main_menu

manager = SaveManager()

class Game:
    def __init__(self):
        self.save_slot = None
        self.player = None
        self.running = True

    def start(self):
        self.save_slot = manager.choose_save_slot()
        self.player = manager.load_game(self.save_slot)
        if not self.player:
            self.player = self.create_character()

        while self.running:
            self.game_menu()

    def create_character(self):
        name = input("Enter your character's name: ")
        player = Player(name)

        manager.save_game(player, self.save_slot)

        return player

    def game_menu(self):
        print(f"\nWelcome to Console RPG -- You are playing as {self.player.name} the {self.player.player_class}")
        print("--- Main Menu ---")
        print("1. Explore")
        print("2. Shop")
        print("3. View Stats")
        print("4. Settings")

        choice = input("> ")

        if choice == "1":
            print("You venture into the wilds...")
        elif choice == "2":
            print("You enter the shop...")
        elif choice == "3":
            self.player.show_stats()
        elif choice == "4":
            settings_choice = display_settings()
            if settings_choice:
                match settings_choice:
                    case 3:
                        display_main_menu()
                        self.start()
        else:
            print("Invalid choice.")