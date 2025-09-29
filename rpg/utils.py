from unittest import case

def display_main_menu():
    print("\n▰▰▰▰▰▰▰▰[ Main Menu | Console RPG ]▰▰▰▰▰▰▰▰")
    print("1. Start")
    print("2. Quit")
    main_menu_choice = int(input("> "))
    match main_menu_choice:
        case 1:
            return main_menu_choice
        case 2:
            print("See ya next time!")
            exit()
        case _:
            print("Invalid Choice...")
    return None

def display_settings():
    print("\n▰▰▰▰▰▰▰▰[ Settings ]▰▰▰▰▰▰▰▰")
    print("1. Game Settings")
    print("2. Character Stats")
    print("3. Exit to Main Menu")
    print("4. Back")
    settings_choice = int(input("> "))
    match settings_choice:
        case 1:
            print("Nothing")
        case 2:
            print("Nothing")
        case 3:
            return settings_choice
        case 4:
            return None
        case "_":
            print("Invalid Choice...")
    return None