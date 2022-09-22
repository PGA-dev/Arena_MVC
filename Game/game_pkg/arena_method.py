'''
Arena Helper Methods
'''



def arena(self):
    pass


def battle_cycle(self, arena_level, _opponents_list):
    self._opponents_list = _opponents_list
    self.arena_level = arena_level
    assert arena_level == arena_level
    # _player and _opponent hp must be further defined, currently are only defining the participating accounts
    _player = _opponents_list['arena_level'] == arena_level
    _player_hp: bool = _player
    _opponent = _opponents_list['arena_level'] == arena_level
    _opponent_hp: bool = _opponents_list['arena_level'] == arena_level and _opponents_list['name'] != "player1"
    _hp_not_null: bool = (_player_hp and _opponent_hp)
    while _hp_not_null:
        if _player_hp == False:
            # run death
            pass
        if _opponent_hp == False:
            # possibly return True when this happens, then use driver code to define the update call
            # run player update and ad to arena_level
            pass
        else:
            break
            pass