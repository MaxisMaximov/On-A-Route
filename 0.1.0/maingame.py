# [Import]
import random, os, time

# [Main Menu]
class startupGame:
    def loadAnimation(self, file):
        animation = "|/-\\"; index = 1; done = 0
        while done<20: print("Loading", file, animation[index % len(animation)], end="\r"); time.sleep(0.1); index += 1; done += 1
        print("\r", file, "Loaded")
    def loadGame(self):
        os.system('cls'); files = ["maingame.py"]
        for file in files: self.loadAnimation(file)
        print("All files loaded"); time.sleep(2); self.startupMenu()
    def startupMenu(self):
        os.system('cls')
        while True:
            action = input("█▀█ █▄ █  ▄▀▄  █▀█ █▀█ █ █ ▀█▀ █▀▀\n█▄█ █ ▀█  █▀█  █▀▄ █▄█ █▄█  █  ██▄\nv0.1.0\n==========\nStart: idstart\n==========\nQuit: idexit\n"); os.system('cls')

            if action == "idstart": mainGame().gameStart()
            elif action == "idexit": exit()
            else: print("Invalid Command\n")

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

# [Set Battle class]
class battle:
    def battleInitiate(self):
        monsterType = random.randint(0, 8)
        if monsterType < 2: setMonster = nme("Baton Zombie", 6, 8)
        if monsterType < 4: setMonster = nme("Armored Zombie", 10, 4)
        if monsterType <= 8: setMonster = nme("Zombie", 6, 4)

        # I have no goddamn pecking idea how, I don't goddamn pecking know why, 
        # but when I tested this earlier in other project it never reset enemy's health
        # What the hell is going on

        print(f"A {setMonster.name} with {setMonster.hp} HP and {setMonster.atk} Attack appears!\nWarning: Invalid commands won't result in action\n") # Some punishment must be made lol
        while True:
            action = input("Attack: idatk\n"); os.system('cls')

            if action == "idatk":
                chance = random.randint(0, 100)
                if chance < gamePlayer.kritChance:
                    setMonster.hp -= gamePlayer.krit
                    print(f"Krit! {gamePlayer.krit} damage!")
                else:
                    setMonster.hp -= gamePlayer.atk
                    print(f"You attack the {setMonster.name}!\nDamage dealt: {gamePlayer.atk}\n")
                if setMonster.hp < 1: print("You win!\n"); break
                else: print(f"Health remaining ({setMonster.name}): {setMonster.hp}\n")
            else: print("Invalid Command\n")

            gamePlayer.hp -= setMonster.atk
            print(f"The {setMonster.name} attacks!\nDamage dealt: {setMonster.atk}\n")
            if gamePlayer.hp < 1: print("Game Over"); exit
            else: print(f"Health remaining (You): {gamePlayer.hp}\n")


# [Main Loop]
class mainGame:
    def gameStart(self):
        while True:
            action = input("Move: idmov\nCheck Stats: idcstat\nExit to menu: idexit\n"); os.system('cls')

            if action == "idmov": 
                print("You moved forward\n")
                gamePlayer.dist += 10
                fork = random.randint(0,2) # Roll a chance for a road fork
                if fork < 1:
                    while True:
                        action = input("You encounter a road fork\nLeft route: idleft\nRight route: idright\n"); os.system('cls')
                        if action == "idleft": print("You take the left route\n"); break
                        elif action == "idright": print("You take the right route\n"); break
                        else: print("Invalid Command\n")

                monster = random.randint(0,2) # Roll a chance for a monster
                if monster < 1: battle().battleInitiate()

            elif action == "idcstat": print(f"Health: {gamePlayer.hp}\nDefense: {gamePlayer.defns}\nAttack: {gamePlayer.atk}\nDistance: {gamePlayer.dist}\n")
            elif action == "idexit":
                action = input("Exit to main menu?\nYes: idexit\nNo: idback\n")
                if action == "idexit": startupGame().startupMenu()
                elif action == "idback": pass
                else: print("Invalid Command\n")
            else: print("Invalid Command\n")
startupGame().loadGame()