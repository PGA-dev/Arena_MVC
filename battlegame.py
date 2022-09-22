# PGA First Week Workshop Assignment
while True:
    # variable assignments
    exit_game = "Exit Game"
    class_wizard = "Wizard"
    class_elf = "Elf"
    class_human = "Human"
    class_cleric = "Cleric"

    class_dragon = "Dragon"

    hp_wizard = 70
    hp_elf = 100
    hp_human = 150
    hp_cleric = 600

    hp_dragon = 300

    damage_wizard = 150
    damage_elf = 100
    damage_human = 20
    damage_cleric = 25

    damage_dragon = 50
# user input
    while True:
        print("1)" + class_wizard)
        print("2)" + class_elf)
        print("3)" + class_human)
        print("4)" + class_cleric)
        print("5)" + exit_game)
# local assignment to my_variables
        char = input("Choose your Character: ")
        character = char.lower()
        if character == "1" or character == "wizard":
            my_class = class_wizard
            my_hp = hp_wizard
            my_dam = damage_wizard
            break
        elif character == "2" or character == "elf":
            my_class = class_elf
            my_hp = hp_elf
            my_dam = hp_elf
            break
        elif character == "3" or character == "human":
            my_class = class_human
            my_hp = hp_human
            my_dam = damage_human
            break
        elif character == "4" or character == "cleric":
            my_class = class_cleric
            my_hp = hp_cleric
            my_dam = damage_cleric
            break
        elif character == "5" or character == "Exit Game" or character == "quit" or character == "Exit":
            print("Exit Game")
            exit()
        else:
            print("Unknown Character")
            continue
    print("")
    print("You chose: " + my_class + "\n" "Health: " +
          str(my_hp) + "\n" + "Damage: " + str(my_dam))
    print("")
# battle
    while True:
        print(my_class + " damages the " + class_dragon)
        hp_dragon = hp_dragon - my_dam
        if hp_dragon <= 0:
            print(class_dragon + " dies and loses the battle!")
            break
        else:
            print(class_dragon + " hp are: " + str(hp_dragon) + " now.")
            print("")
        print(class_dragon + " damages the " + my_class)
        my_hp = my_hp - damage_dragon
        if my_hp <= 0:
            print(my_class + " dies and loses the battle!")
            break
        else:
            print(my_class + " hp is now: " + str(my_hp))
            print("")
            continue
# restart
    restar = input("Play again? y/n ")
    restart = restar.lower()
    if restart == 'y' or restart == "yes":
        continue
    else:
        print("Goodbye")
        exit()
