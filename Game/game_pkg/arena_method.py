'''
Arena Helper Methods
'''



from ast import List
import random


def arena(self):
    pass

def char_num(character_list):
    return random.randint(0,len(character_list))


def battle_cycle(character_list: List):
    _character1 = character_list[char_num]

    _character2 = character_list[0, random.randint(0,len(character_list))]
    # _player and _opponent hp must be further defined, currently are only defining the participating accounts
    _character1_hp = character_list[0:'hp']
    _character2_hp = character_list[0:'hp']
    _hp_not_null: bool = (_character1_hp and _character2_hp)
    while _hp_not_null:
        if _character1_hp == False:
            # run death
            pass
        if _character2_hp == False:
            # possibly return True when this happens, then use driver code to define the update call
            # run player update and ad to arena_level
            pass
        else:
            break
            pass