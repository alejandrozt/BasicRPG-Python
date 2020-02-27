import random
import json

# DmgTypes: 0 - Phisical / 1 - Fire / 2 - Cold / 3 - Electric

# {id : ["Name", SpeedMod, BaseDmg, DmgType]}
dictMonsterAttacks =    {
                        1 : ["Punch", 0, 4, 0], 
                        2 : ["Kick", -1, 6, 0]
                        }

# {id : ["Name", HPmax, AC, Speed, [Attack1, Attack2, ...]]}
dictMonsters =  {
                1 : ["Goblin", 7, 10, 12, [1, 2]], 
                2 : ["Deserter", 12, 12, 9, [1, 2]]
                }

def getRandomMonster():
    return (dictMonsters[random.choice(list(dictMonsters.keys()))])
