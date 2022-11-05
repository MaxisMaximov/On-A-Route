import random, pickle
def SaveManager():

    def saveStuff(data):
        saveFile = open("saveFile.json", "wb+")
        pickle.dump(data, saveFile)

    def loadStuff():
        saveFile = open("saveFile.json", "rb+")
        data = pickle.load(saveFile)
        return data

    dataToSave = {"Ze Data": ["lol", "bla", "1.19.1 is shit"]}
    print(dataToSave)
    saveStuff(dataToSave)
    stuff = loadStuff()
    print(stuff)
    print(stuff["Ze Data"])
    otherData = {"Ze Data": ["new thingy", "lol", "1.19.1 is still shit"], "New data": ["moar", "idk"]}
    stuff = loadStuff()
    print(stuff)
    stuff.update(otherData)
    print(stuff["Ze Data"])
    saveStuff(stuff)
    moarstuff = loadStuff()
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

