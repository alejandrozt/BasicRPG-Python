import random
import json
import GenMonster

content =   {
            1 : ["Small Barrel", (1,1), "random"], 
            2 : ["Barrel", (1,1), "random"], 
            3 : ["Fountain", (1,1), "random"], 
            4 : ["Small library", (1,1), "random"], 
            5 : ["Library", (1,1), "random"]
            }

treasure =  {
            1 : ["Small Box", (1,1), "random"],
            2 : ["Big Box", (1,1), "random"],
            3 : ["Chest", (1,1), "random"],
            4 : ["Big Pile", (1,1), "random"]
            }

rooms = {}

def generateId():
    id = ""
    for x in range(8):
        id = id + str(random.randint(0,9))
    return id

def defineDimensions():
    return (random.randrange(4,8), random.randrange(4,8))

def selectThings(content : dict, treasure : dict):
    selectedThings = {}
    id = 0
    for x in range(5):
        randSelector = random.randrange(1,2)
        if randSelector == 1:
            thing = random.choice(list(content.keys()))
            selectedThings[id] = (thing, content[thing])
        elif randSelector == 2:
            thing = random.choice(list(treasure.keys()))
            selectedThings[id] = (thing, treasure[thing])
        id += 1
    return selectedThings

def selectMonsters(cant : int):
    selectedMonsters = {}
    id = 0
    for x in range(cant):
        selectedMonsters[id] = GenMonster.getRandomMonster()
        id += 1
    return selectedMonsters

def organizeThings(room : dict, things : dict, monsters : dict):
    for thing in things:
        pos = random.choice(sorted(list(room.keys())))
        room[pos] = things[thing][1]
    for monster in monsters:
        pos = random.choice(sorted(list(room.keys())))
        # while pos != "empty":
        #     pos = random.choice(sorted(list(room.keys())))
        room[pos] = monsters[monster]
    return room

def generateGraphicEnviroment(organizedRoom : dict):
    graphicRoom = {}
    for step in organizedRoom.keys():
        graphicRoom[step] = organizedRoom[step][0][:3]
    return graphicRoom

genId = generateId()

print(genId)

dimensions = defineDimensions()

room = {}

things = selectThings(content, treasure)
monsters = selectMonsters(2)

print(things)

for x in range(dimensions[0]):
    for y in range(dimensions[1]):
        room[str(x) + "-" + str(y)] = "empty"

organizedRoom = organizeThings(room, things, monsters)

for x in range(dimensions[0]):
    for y in range(dimensions[1]):
        key = str(x) + "-" + str(y)
        print((organizedRoom[key]), end="\t|\t")
    print("\n")

graphicRoom = generateGraphicEnviroment(organizedRoom)
for x in range(dimensions[0]):
    for y in range(dimensions[1]):
        key = str(x) + "-" + str(y)
        print((graphicRoom[key]), end="\t|\t")
    print("\n")

# with open("rooms.json", "a") as f:
#     json.dumps(rooms)
#     jsonF[genId] = rooms[genId]
#     json.dump(rooms, f)

# with open("rooms.json", "r") as f:
#     textF = f.read()
#     jsonF = json.loads(textF)

# with open("rooms.json", "w") as f:
#     json.dumps(rooms)
#     jsonF[genId] = rooms[genId]
#     json.dump(jsonF, f)

# print(sorted(list(jsonF.keys())))