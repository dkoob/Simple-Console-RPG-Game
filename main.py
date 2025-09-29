from rpg.game import Game
from rpg.save_systems import init_slots, SaveManager
from rpg.utils import display_main_menu

def main():
    init_slots()
    main_menu_choice = display_main_menu()
    match main_menu_choice:
        case 1:
            print()
            game = Game()
            game.start()
        case _:
            return

if __name__ == '__main__':
    main()