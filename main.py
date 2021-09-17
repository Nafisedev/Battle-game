from classes.game import Person, bcolors
from classes.magic import Spell

# Create black magic
fire = Spell("Fire", 10, 100, "black")
thunder = Spell("Thunder", 10, 100, "black")
blizzard = Spell("Blizzard", 10, 100, "black")
meteor = Spell("Meteor", 20, 200, "black")
quake = Spell("Quake", 14, 140, "black")

# Create white magic
cure = Spell("Cure", 12, 120, "white")
cura = Spell("Cura", 18, 200, "white")

#Instantiate People
players = Person(460, 65, 60, 34, [fire, thunder, blizzard, meteor, cure, cura])
enemy = Person(1200, 65, 45, 25, [])

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

        print(magic_choice)
        spell = players.magic[magic_choice]
        magic_dmg = spell.generate_damage()

        current_mp = players.get_mp()

        if spell.cost > current_mp:
            print(bcolors.FAIL + "\nNot enough MP" + bcolors.ENDC)
            continue

        players.reduce_mp(spell.cost)

        if spell.type == "white":
            players.heal(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " heals for", str(magic_dmg), "HP." + bcolors.ENDC)
        elif spell.type == "black":
            enemy.take_damage(magic_dmg)
            print(bcolors.OKBLUE + "\n" + spell.name + " deals " + str(magic_dmg), "Point of damage" + bcolors.ENDC)


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





