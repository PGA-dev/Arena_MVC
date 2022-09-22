from game_pkg import c_r_u_d

'''model'''
class Character_Model(object):

    def __init__(self, character_list_elements):
        self._char_type = "warrior"
        self.create_chars(character_list_elements)

    @property
    def char_type(self):
        return self._char_type

    @char_type.setter
    def char_type(self, new_char_type):
        self._char_type = new_char_type

    def create_char(self, name, ac, damage, hp, to_hit):
        c_r_u_d.create_char(name, ac, damage, hp, to_hit)


    def create_chars(self, opponent_list):
        c_r_u_d.create_chars(opponent_list)

    def read_char(self, name):
        return c_r_u_d.read_char(name)

    def read_chars(self):
        return c_r_u_d.read_chars()

    def update_char(self, name, ac, damage, hp, to_hit):
        c_r_u_d.update_char(name, ac, damage, hp, to_hit)

    def return_char_item(self, name, ac, damage, hp, to_hit):
        c_r_u_d.read_char(name)

    def delete_char(self, name):
        c_r_u_d.delete_char(name)
