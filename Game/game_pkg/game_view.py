

'''View'''

# TODO Define view objects for Arena, player sheet, and opponent sheet


class Game_View(object):


    @staticmethod
    def vl_display_character_list(char_type, opponents_list: list):
        print(f"\n")
        print(f"--- ARENA {char_type.upper()} LIST ---")
        print(f"\n")
        char: dict
        for char in opponents_list:
            print(f"{char_type.upper()}'s Name: {char['name'].upper()}")
            for key in char.keys():
                if char[key] == char['name']:
                    print(f"")
                else:
                    print(f"{key.upper()}: {char[key]}")
            print(f"\n\n")

    @staticmethod
    def vl_display_character_filled(char_type, opponents_list: list):
        print(f"\n")
        print(f"--- ARENA {char_type.upper()} LIST ---")
        print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print(f"\n")
        char: dict
        for char in opponents_list:
            print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            print(f"{char_type.upper()}'s Name: {char['name'].upper()}")
            for key in char.keys():
                if char[key] == char['name']:
                    print(
                        f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||"
                    )
                else:
                    print(f"{key.upper()}: {char[key]}")
            print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
            print(f"\n")

    @staticmethod
    def show_char(char_type, char_name, char: dict):
        print(f"\n")
        print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print(f"Arena {char_type.upper()} PLAYER SHEET     ")
        print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print(f"Name: {char_name.upper()}")
        print(f"\n")
        print(f"Armor Class: {char.get('ac')}")
        print(f"Damage: {char.get('damage')}")
        print(f"Hit Points: {char.get('hp')}")
        print(f"To Hit: {char.get('to_hit')}")
        print(f"\n")
        print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

    @staticmethod
    def display_missing_char_error(char, err):
        print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print(f" {char.upper()} is not available, not in our db!")
        print(f"{err.args[0]}")
        print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

    @staticmethod
    def display_char_already_stored_error(char, char_type, err):
        print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print(f"{char.upper()} is already a {char_type} in our Arena list!")
        print(f"{err.args[0]}")
        print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

    @staticmethod
    def display_char_not_yet_stored_error(char, char_type, err):
        print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print(f"{char.upper()} is not currently a {char_type.upper()} in our Arena {char_type}'s list. Please insert it first!")
        print(f"{err.args[0]}")
        print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

    @staticmethod
    def display_char_stored(char, char_type):
        print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print(f"{char.upper()} has been added to our Arena {char_type}'s list!")
        print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

    @staticmethod
    def display_change_char_type(older, newer):
        print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print('Change char type from "{}" to "{}"'.format(older, newer))
        print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

    @staticmethod
    # update to all passed params
    def new_arena_char_updated(char, n_ac, o_ac, n_damage, o_damage, o_hp, n_hp, n_to_hit, o_to_hit):
        print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print(
            f"We changed {char} Old Hit Points: {o_hp} New Hit Points: {n_hp}")
        print(
            f"We changed {char} Old Damage : {o_damage} New Damage: {n_damage}")
        print(
            f"We changed {char} Old To Hit: {o_to_hit} New To Hit: {n_to_hit}")
        print(f"We changed {char} Old To Hit: {o_ac} New To Hit: {n_ac}")
        print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

    @staticmethod
    def display_char_deletion(name):
        print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print(
            f" {name} is dead, so we have just removed {name} from our Arena")
        print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")

# need controller and model settings
    @staticmethod
    def display_player_char_death(name):
        print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
        print(
            f" {name} is dead, would you like to play again?")
        print(f"||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||")
