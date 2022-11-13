import random, pickle
class SaveManager():
    def saveStuff(self, data):
        saveFile = open("saveFile.json", "wb+")
        pickle.dump(data, saveFile)

    def loadStuff(self):
        saveFile = open("saveFile.json", "rb+")
        data = pickle.load(saveFile)
        return data

    def test(self):
        dataToSave = {"Ze Data": ["lol", "bla", "1.19.1 is shit"]}
        print(dataToSave)
        self.saveStuff(dataToSave)
        stuff = self.loadStuff()
        print(stuff)
        print(stuff["Ze Data"])
        otherData = {"Ze Data": ["new thingy", "lol", "1.19.1 is still shit"], "New data": ["moar", "idk"]}
        stuff = self.loadStuff()
        print(stuff)
        stuff.update(otherData)
        print(stuff["Ze Data"])
        self.saveStuff(stuff)
        moarstuff = self.loadStuff()
        print(moarstuff)
        print(__file__)
def someStuff():
    a = 100
    b = 100
    c = 50
    a -= int(b - (b * c)/100)
    print(a)

    print(round(random.uniform(1.00, 10.00), 2))
    class stuff:
        def __init__(self, number, name):
            self.number = number
            self.name = name
    randomStuff = [(5, "lol"), (10, "lmao")]
    thingy = random.choices(randomStuff, weights=[90, 5])
    anotherThingy = stuff(*thingy)
    print(anotherThingy)

class lol():
    def __init__(self):
        self.dataList = []
        self.dataDict = {"randomText": ["lol", "iddqd", 6, "Blah", "Blah", "iddqd"]}

someList = {"randomText": ["lol", "iddqd", 6, "Blah", "Blah", "iddqd"]}
print(someList)
SaveManager().saveStuff(someList)
SaveManager().loadStuff
secondList = [*someList["randomText"]]
print(secondList)
lol.dataList = secondList
print(lol.dataList, "Data in class")
#lol.dataDict = someList
print(*lol.dataDict["randomText"])

print(random.choices(lol.dataList, (50, 90, 20, 30, 30, 70)))