from classes.game import Person, bcolors


magic = [{"name": "Fire", "cost": 10, "dmg": 100},
         {"name": "Thunder", "cost": 12, "dmg": 124},
         {"name": "Blizzard", "cost": 10, "dmg": 100}]


players = Person(460, 65, 60, 34, magic)
enemy = Person(1200, 65, 45, 25, magic)

running = True
i = 0
print(bcolors.FAIL + bcolors.BOLD + "AN ENEMY ATTACK!" + bcolors.ENDC)

while running:
    print("===========================")
    players.choose_action()
    choice = input("Choose action:")
    index = int(choice) - 1

    if index == 0:
        dmg = players.generate_damage()
        enemy.take_damage(dmg)
        print("You attack for", dmg, "Point of damage.")
    elif index == 1:
        players.choose_magic()
        magic_choice = int(input("Choose magic: ")) - 1
        magic_dmg = players.generate_spell_damage(magic_choice)
        spell = players.get_spell_name(magic_choice)
        cost = players.get_spell_mp_cost(magic_choice)

        current_mp = players.get_mp()

        if cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP" + bcolors.ENDC)
            continue
        players.reduce_mp(cost)
        enemy.take_damage(magic_dmg)
        print(bcolors.OKBLUE + "\n" + spell + " deals " + str(magic_dmg), "Point of damage" + bcolors.ENDC)


    enemy_choice = 1

    enemy_dmg = enemy.generate_damage()
    players.take_damage(enemy_dmg)
    print("Enemy attack for", enemy_dmg)

    print("---------------------------")
    print("Enemy HP: ", bcolors.FAIL + str(enemy.get_hp()) + "/" + str(enemy.get_max_hp()) + bcolors.ENDC + "\n")

    print("Your HP: ", bcolors.OKGREEN + str(players.get_hp()) + "/" + str(players.get_max_hp()) + bcolors.ENDC)
    print("Your MP: ", bcolors.OKBLUE + str(players.get_mp()) + "/" + str(players.get_max_mp()) + bcolors.ENDC + "\n")



    if enemy.get_hp() == 0:
        print(bcolors.OKGREEN + "You win!" + bcolors.ENDC)
        running = False
    elif players.get_hp() == 0:
        print(bcolors.FAIL + "You lost!" + bcolors.ENDC)
        running = False





