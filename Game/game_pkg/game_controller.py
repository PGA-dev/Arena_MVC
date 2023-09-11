'''General Game Character Controller
    ---uses model and view
'''

# from game_pkg import game_model
# from game_pkg import game_view
from game_pkg import exceptions as mvc_exc




class Game_Controller(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view


    def show_chars(self, _no_format=False):
        chars = self.model.read_chars()
        char_type = self.model.char_type
        if _no_format:
            self.view.vl_display_character_list(char_type, chars)
        else:
            self.view.vl_display_character_filled(char_type, chars)

    def show_char(self, char_name):
        try:
            char = self.model.read_char(char_name)
            char_type = self.model.char_type
            self.view.show_char(char_type, char_name, char)
        except mvc_exc.CharNotStored as e:
            self.view.display_missing_char_error(char_name, e)

    def insert_char(self, name, ac, damage, hp, to_hit):
        assert hp >= 0, "character must have more than 0 hp"
        char_type = self.model.char_type
        try:
            self.model.create_char(
                name, ac, damage, hp, to_hit)
            self.view.display_char_stored(name, char_type)
        except mvc_exc.CharAlreadyStored as e:
            self.view.display_char_already_stored_error(name, char_type, e)


    def update_char(self, name, ac, damage, hp, to_hit):
        #assert hp >= 0, 'quantity must be greater than or equal to 0'
        char_type = self.model.char_type

        try:
            older = self.model.read_char(name)
            self.model.update_char(
                name, ac, damage, hp, to_hit)
            self.view.new_arena_char_updated(
                name, older["ac"], older["damage"], older["hp"], older["to_hit"], ac, damage, hp, to_hit)  # need to update view logic
        except mvc_exc.CharNotStored as e:
            self.view.display_char_not_yet_stored_error(name, char_type, e)
            # if the item is not yet stored and we performed an update, we have
            # 2 options: do nothing or call insert_item to add it.
            # self.insert_item(name, arena_level, damage, hp, to_hit, strength, dexterity, constitution)

    def update_char_type(self, new_char_type):
        old_char_type = self.model.char_type
        self.model.char_type = new_char_type
        self.view.display_change_char_type(old_char_type, new_char_type)

    def delete_char(self, name):
        char_type = self.model.char_type
        try:
            self.model.delete_char(name)
            self.view.display_char_deletion(name)
        except mvc_exc.CharNotStored as e:
            self.view.display_char_not_yet_stored_error(name, char_type, e)

    def player_death(self, name):
        pass
