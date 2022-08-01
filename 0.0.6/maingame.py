# [Import]
import random
import os

# [Main Menu]
while True:
    action = input("On A Route v0.0.6\n"
    "Start: idstart\n"
    "Quit: idexit\n")
    os.system('cls')

    if action == "idstart":
        break

    elif action == "idexit":
        exit

    else:
        print("Invalid Command\n")

# [Set Player]
class player:
    def __init__(self, hp, defns, atk, krit, kritChance, dist):   
        self.hp = hp
        self.defns = defns
        self.atk = atk
        self.krit = krit
        self.kritChance = kritChance
        self.dist = dist

gamePlayer = player(50, 10, 4, 12, 20, 0)

# [Set Enemy class]
class nme:
    def __init__(self, name, hp, atk):
        self.name = name
        self.hp = hp
        self.atk = atk

# [Set Battle Def]
def battle():
    monsterType = random.randint(0, 8)

    if monsterType < 2:
        setMonster = nme("Baton Zombie", 6, 8)

    if monsterType < 4:
        setMonster = nme("Armored Zombie", 10, 4)

    if monsterType <= 8:
        setMonster = nme("Zombie", 6, 4)

    # I have no goddamn pecking idea how, I don't goddamn pecking know why, 
    # but when I tested this earlier in other project it never reset enemy's health
    # What the hell is going on

    print(f"A {setMonster.name} with {setMonster.hp} HP and {setMonster.atk} Attack appears!\n"
    "Warning: Invalid commands won't result in action\n") # Some punishment must be made lol
    while True:
        action = input("Attack: idatk\n")
        os.system('cls')

        if action == "idatk":

            chance = random.randint(0, 100)
            if chance < gamePlayer.kritChance:
                setMonster.hp -= gamePlayer.krit
                print(f"Krit! {gamePlayer.krit} damage!")
            else:
                setMonster.hp -= gamePlayer.atk
                print(f"You attack the {setMonster.name}!\n"
                f"Damage dealt: {gamePlayer.atk}\n")

            if setMonster.hp < 1:
                print("You win!\n")
                break
            else:
                print(f"Health remaining ({setMonster.name}): {setMonster.hp}\n")
        else:
            print("Invalid Command\n")

        gamePlayer.hp -= setMonster.atk
        print(f"The {setMonster.name} attacks!\n"
        f"Damage dealt: {setMonster.atk}\n")

        if gamePlayer.hp < 1:
            print("Game Over")
            exit
        else:
            print(f"Health remaining (You): {gamePlayer.hp}\n")


# [Main Loop]
while True:
    action = input("Move: idmov\n"
    "Check Stats: idcstat\n")
    os.system('cls')

    if action == "idmov":
        print("You moved forward\n")
        gamePlayer.dist += 10

        fork = random.randint(0,2) # Roll a chance for a road fork
        if fork < 1:
            while True:
                action = input("You encounter a road fork\n"
                "Left route: idleft\n"
                "Right route: idright\n")
                os.system('cls')

                if action == "idleft":
                    print("You take the left route\n")
                    break

                elif action == "idright":
                    print("You take the right route\n")
                    break

                else:
                    print("Invalid Command\n")

        monster = random.randint(0,2) # Roll a chance for a monster
        if monster < 1:
            battle()


    elif action == "idcstat":
        print(f"Health: {gamePlayer.hp}\n"
            f"Defense: {gamePlayer.defns}\n"
            f"Attack: {gamePlayer.atk}\n"
            f"Distance: {gamePlayer.dist}\n")
        
    else:
        print("Invalid Command\n")