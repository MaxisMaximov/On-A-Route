import os, random, pickle
class inventory:
    invList = []
    def __init__(self):
        # Index coding: XXX-XXX-XX-XXX  |  Type-Area-Enemy_Group-Item_In_Group
        # Types -- Items: itm, Enemies: nme, Bosses: bos
        # The enemies are sorted by their probability, highest probability first and lowest last

        # Yes I know I can use UUID but that one's too big for this game lmao
        # Also I don't expect to have more than 999 areas, 99 enemy groups
        # in each of them and 999 items in each group
        
        self.itemIndex = {
            # Zombie Group
            "itm-001-01-001":["Cloth"],
            "itm-001-01-002":["Broken Helmet"],
            "itm-001-01-003":["Baton"],
            # Mutated Group
            "itm-001-02-001":["Pulsing Flesh"],
            "itm-001-02-002":["Wolf Skin"],
            "itm-001-02-003":["Snake Poison"],
            }

        self.lootIndex = {
            "nme-001-01-001": ["itm-001-01-001"],  # Zombie
            "nme-001-01-002": ["itm-001-01-001", "itm-001-01-002"],  # Armored Zombie
            "nme-001-01-003": ["itm-001-01-001", "itm-001-01-003"],  # Baton Zombie
            "nme-001-02-001": ["itm-001-02-001"],  # Mutated Zombie
            "nme-001-02-002": ["itm-001-02-001", "itm-001-02-002"],  # Mutated Wolf
            "nme-001-02-003": ["itm-001-02-003"]  # Mutated Snake
        }

    def lootStuff(self, lootID):
        loot = self.lootIndex[lootID]
        item = random.choice(loot)
        self.invList.append(item)

    def loadInv(self, data):
        if data == "resetInv":
            self.invList = []
            return
        for item in data:
            self.invList.append(item)

    def invMode(self):
        while True:
            action = input("Inventory Mode\nCheck Inventory: idcinv\nThrow out item: idtrash\nExit: idexit\n"); os.system('cls')

            if action == "idcinv":
                if len(self.invList) > 0:
                    print("[Item]")
                    tmpList = self.invList.copy()
                    for item in tmpList:
                        xValue = "x" + str(tmpList.count(item))
                        for cItem in tmpList:
                            if cItem == item:
                                tmpList.remove(item)
                        gotItem = self.itemIndex[item]
                        print(gotItem[0], xValue)
                    print("______")
                else:
                    print("No items in Inventory")
            elif action == "idtrash":
                itemToDel = input("Which item do you want to throw out?\n")
                for id, name in self.itemIndex.items():
                    if name[0] == itemToDel:
                        itemExists = True
                        trashItem = id
                        break
                    else:
                        itemExists = False
                        trashItem = "null"
                if itemExists == True and trashItem in self.invList:
                    print(f"You threw out {itemToDel}")
                    self.invList.remove(trashItem)
                else:
                    print("Invalid item name")
            elif action == "idexit":
                print("Exited from Inventory Mode")
                break
            else: print("Invalid Command\n")

def invModeGo():
    inventory().invMode()