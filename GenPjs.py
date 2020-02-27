import random
import json
import names

dicStats = {0 : "Strength", 1 : "Dexterity", 2 : "Constitution", 3 : "Inteligence", 4 : "Wisdom", 5 : "Charisma"}
fantasyRaces = ["Elf", "Dark elf", "Dwarf", "Human", "Gnome", "Halfling"]
dicStatMod =   {
                "Beefy boi" : (0, 2), "Stronk" : (0, 4), 
                "Gotta Go Fast" : (1, 2), "Acrobat's life" : (1, 4), 
                "Square" : (2, 2), "Spherical, but that's ok" : (2, 4), 
                "Four-eyes" : (3, 2), "Smartass" : (3, 4), 
                "Sens8" : (4, 2), "One with all" : (4, 4), 
                "The Hahas" : (5, 2), "The soul of the party" : (5, 4)
            }


def ranStatBloq():
    statBloq = []
    for x in range(6):
        statBloq.append(random.randint(8, 16))
    return statBloq

def getStatMod(dicStatMod : dict):
    mod = random.choice(list(dicStatMod.keys()))
    return (mod, dicStatMod[mod])

pjs = {}

random.shuffle(fantasyRaces)

statBloq = ranStatBloq()
modsAplicados = []
cantMod = random.randint(1,3)
for num in range(cantMod):
    modActual = getStatMod(dicStatMod)
    if (modActual[1])[0] not in modsAplicados:
        if (modActual[1])[1] > 0:
            modsAplicados.append((modActual[0] + ": +" + str((modActual[1])[1]) + " " + dicStats[(modActual[1])[0]]))
        else:
            modsAplicados.append((modActual[0] + ": -" + str((modActual[1])[1]) + " " + dicStats[(modActual[1])[0]]))
        statBloq[(modActual[1])[0]] += (modActual[1])[1]
    else:
        num -= 1
genName = names.get_first_name()
pjs[genName] = (fantasyRaces.pop(0), statBloq, modsAplicados)

print(pjs)

with open("pjs.json", "r") as f:
    textF = f.read()
    jsonF = json.loads(textF)

with open("pjs.json", "w") as f:
    json.dumps(pjs)
    jsonF[genName] = pjs[genName]
    json.dump(jsonF, f)

print(sorted(list(jsonF.keys())))

