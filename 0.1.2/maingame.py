# [Import]
import random, os, time, pickle

# [Main Menu]
class startupGame:
    def __init__(self):  # This is really only for paths lol
        self.saveDir = str(os.path.join(__file__, "..", "..", "oarSaves"))
        self.savePath = str(os.path.join(self.saveDir, "saveFile.json"))
    def loadAnimation(self, file):
        animation = "|/-\\"; index = 1; done = 0
        while done<20: print("Loading", file, animation[index % len(animation)], end="\r"); time.sleep(0.1); index += 1; done += 1
        print("\r", file, "Loaded       ")  # Now fixed
    def loadGame(self):  # I know this is completely pointless but it's quite fun
        os.system('cls'); files = ["maingame.py"]
        for file in files: self.loadAnimation(file)
        print("All files loaded"); time.sleep(2); self.startupMenu()
    def startupMenu(self):
        os.system('cls')
        while True:
            action = input("█▀█ █▄ █  ▄▀▄  █▀█ █▀█ █ █ ▀█▀ █▀▀\n█▄█ █ ▀█  █▀█  █▀▄ █▄█ █▄█  █  ██▄\nv0.1.2\n==========\nStart: idstart\n==========\nQuit: idexit\n"); os.system('cls')

            if action == "idstart": self.loadSaves(); mainGame().gameStart()
            elif action == "idexit": exit()
            else: print("Invalid Command\n")
    def loadSaves(self): # TODO: Clean up and make this a sepparate file once there's too much stuff to save
        if not os.path.exists(self.saveDir): os.makedirs(self.saveDir); print("Save Directory created", self.saveDir)  # If directory doesn't exist, create
        global gamePlayer; open(self.savePath, "a")  # This one thing gave me so much pain
        if os.stat(self.savePath).st_size == 0: gamePlayer = player(50, 10, 4, 12, 20, 0); self.saveInfo()  # If file empty, write base info into it
        else: data = pickle.load(open(self.savePath, "rb+"));gamePlayer = player(*data["Player"])  # If file has something, load it into the system
    def saveInfo(self): p = gamePlayer; data = {"Player": [p.hp, p.defns, p.atk, p.krit, p.kritChance, p.dist]}; pickle.dump(data, open(self.savePath, "wb"))
    def newGame(self): global gamePlayer; gamePlayer = player(50, 10, 4, 12, 20, 0); self.saveInfo()
        
# [Set Player]
class player:
    def __init__(self, hp, defns, atk, krit, kritChance, dist):   
        self.hp = hp
        self.defns = defns
        self.atk = atk
        self.krit = krit
        self.kritChance = kritChance
        self.dist = dist

# [Set Enemy class]
class nme:
    def __init__(self, name, hp, defns, atk):
        self.name = name
        self.hp = hp
        self.defns = defns
        self.atk = atk

# [Set Battle class]
class battle:
    def battleInitiate(self):
        monsterType = random.randint(0, 100)
        if monsterType < 20: setMonster = nme("Mutated Snake", 6, 4, 10)
        elif monsterType < 35: setMonster = nme("Mutated Wolf", 8, 12, 6)
        elif monsterType < 45: setMonster = nme("Mutated Zombie", 12, 5, 8)
        elif monsterType < 50: setMonster = nme("Baton Zombie", 6, 0, 8)
        elif monsterType < 75: setMonster = nme("Armored Zombie", 6, 8, 4)
        elif monsterType <= 100: setMonster = nme("Zombie", 6, 2, 4)
        # Instead of changing the rates to accomodate more enemies it's easier to just set percentage value
        # Also this part took me a good while to figure out why Zombie was being given out all the time lol


        # I have no goddamn pecking idea how, I don't goddamn pecking know why, 
        # but when I tested this earlier in other project it never reset enemy's health
        # What the hell is going on

        print(f"A {setMonster.name} with {setMonster.hp} HP, {setMonster.defns} Defense and {setMonster.atk} Attack appears!\nWarning: Invalid commands won't result in action\n") # Some punishment must be made lol
        while True:
            action = input("Attack: idatk\n"); os.system('cls')

            if action == "idatk":
                chance = random.randint(0, 100)
                if chance < gamePlayer.kritChance:
                    setMonster.hp -= gamePlayer.krit
                    print(f"Krit! {gamePlayer.krit} damage!")
                else:
                    setMonster.hp -= gamePlayer.atk - int((gamePlayer.atk * setMonster.defns)/100)
                    print(f"You attack the {setMonster.name}!\nDamage dealt: {gamePlayer.atk}\n")
                if setMonster.hp < 1: print("You win!\n"); break
                else: print(f"Health remaining ({setMonster.name}): {setMonster.hp}\n")
            else: print("Invalid Command\n")

            gamePlayer.hp -= setMonster.atk - int((setMonster.atk * gamePlayer.defns)/100)
            print(f"The {setMonster.name} attacks!\nDamage dealt: {setMonster.atk}\n")
            if gamePlayer.hp < 1: print("Game Over"); startupGame().newGame(); input("Press any key to Exit"); exit()
            else: print(f"Health remaining (You): {gamePlayer.hp}\n")


# [Main Loop]
class mainGame:
    def gameStart(self):
        while True:
            startupGame().saveInfo()
            action = input("Move: idmov\nCheck Stats: idcstat\nExit to menu: idexit\n"); os.system('cls')

            if action == "idmov": 
                print("You moved forward\n")
                gamePlayer.dist += 10
                fork = random.randint(0,2)  # Roll a chance for a road fork
                if fork < 1:
                    while True:
                        action = input("You encounter a road fork\nLeft route: idleft\nRight route: idright\n"); os.system('cls')
                        if action == "idleft": print("You take the left route\n"); break
                        elif action == "idright": print("You take the right route\n"); break
                        else: print("Invalid Command\n")

                monster = random.randint(0,2)  # Roll a chance for a monster
                if monster < 1: battle().battleInitiate()

            elif action == "idcstat": print(f"Health: {gamePlayer.hp}\nDefense: {gamePlayer.defns}\nAttack: {gamePlayer.atk}\nDistance: {gamePlayer.dist}\n")
            elif action == "idexit":
                action = input("Exit to main menu?\nYes: idexit\nNo: idback\n")
                if action == "idexit": startupGame().startupMenu()
                elif action == "idback": pass  # This is unnececary but otherwise it would print the else thing, and Python doesn't like empty if/elif/else statements
                else: print("Invalid Command\n")
            else: print("Invalid Command\n")
startupGame().loadGame()