'''controller_instance'''
'''name, arena_level, damage, hp, to_hit, strength, ac'''


from game_pkg.c_r_u_d import DB_name, connect_to_db, connect, create_table, tuple_convert, update_char, insert_char, insert_chars, IntegrityError
from game_pkg import exceptions as mvc_exc
from game_pkg import arena_method as a_h_m
from game_pkg.game_controller import Game_Controller 
from game_pkg.game_model import ModelSQLite
from game_pkg.game_view import Game_View





'''
Driver code Entry Point for Game
'''

def main():

    table_name = 'chars'
    conn = connect_to_db()  # in-memory database
    #conn = connect_to_db(DB_name)  # physical database (i.e. a .db file)

    create_table(conn, table_name)




    # # Main Data List of Dictionaries
    # opponents: list = [{"name": "Brute", "ac": 3, "damage": 75, "hp": 200, "to_hit": 15},
    #                    {"name": "Inside", "ac": 8, "damage": 45, "hp": 100, "to_hit": 65},
    #                    {"name": "Dodge", "ac": 15, "damage": 35, "hp": 75, "to_hit": 75},
    #                    {"name": "Right_Hook", "ac": 7, "damage": 50, "hp": 100, "to_hit": 35},
    #                    {"name": "Feet", "ac": 5, "damage": 60, "hp": 120, "to_hit": 25}]


    # character1 = Game_Controller(ModelSQLite(opponents), Game_View())
    # character2 = Game_Controller(ModelSQLite(opponents), Game_View())
    # #monster1 = Controller(ModelBasic(my_items2), View())
    # character2.show_char("Brute")
    # character1.show_chars()
    # # character1.insert_char("supremecommander", 5, 75, 200, 45)
    # # character1.show_chars()
    # # character1.delete_char("supremecommander")
    # # character1.show_char("elite")
    # # character1.show_chars()
    # # character1.show_char("bob")
    # # character1.update_char("supremecommander", 10, 75, 250, 75)
    # # character1.show_char("supremecommander")


if __name__ == '__main__':
    main()
