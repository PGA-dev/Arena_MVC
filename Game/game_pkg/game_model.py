from game_pkg import c_r_u_d
from game_pkg import exceptions as mvc_exc
'''model'''


class ModelSQLite(object):

    def __init__(self, character_list_elements):
        self._char_type = 'Warrior'
        self._connection = c_r_u_d.connect_to_db(c_r_u_d.DB_name)
        c_r_u_d.create_table(self.connection, self._char_type)
        self.create_chars(character_list_elements)

    @property
    def connection(self):
        return self._connection

    @property
    def char_type(self):
        return self._char_type

    @char_type.setter
    def item_type(self, new_char_type):
        self._char_type = new_char_type

    def create_char(self, name, ac, damage, hp, to_hit):
        c_r_u_d.insert_char(
            self.connection, name, ac, damage, hp, to_hit, table_name=self.char_type)

    def create_chars(self, chars):
        c_r_u_d.insert_chars(
            self.connection, chars, table_name=self.char_type)

    def read_char(self, name):
        return c_r_u_d.select_char(
            self.connection, name, table_name=self.char_type)

    def read_chars(self):
        return c_r_u_d.select_all(
            self.connection, table_name=self.char_type)

    def update_char(self, name, ac, damage, hp, to_hit):
        c_r_u_d.update_char(
            self.connection, name, ac, damage, hp, to_hit, table_name=self.char_type)

    def delete_char(self, name):
        c_r_u_d.delete_char(
            self.connection, name, table_name=self.char_type)





