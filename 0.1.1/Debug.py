import pickle

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