#cost,dmg,armor
from itertools import product

weapons = {
    "Dagger":      (8, 4, 0),
    "Shortsword":  (10, 5, 0),
    "Warhammer":   (25, 6, 0),
    "Longsword":   (40, 7, 0),
    "Greataxe":    (74, 8, 0)
}

armor = {
    "Leather":     (13, 0, 1),
    "Chainmail":   (31, 0, 2),
    "Splintmail":  (53, 0, 3),
    "Bandedmail":  (75, 0, 4),
    "Platemail":   (102, 0, 5)
}

rings = {
    "Damage +1":   (25, 1, 0),
    "Damage +2":   (50, 2, 0),
    "Damage +3":   (100, 3, 0),
    "Defense +1":  (20, 0, 1),
    "Defense +2":  (40, 0, 2),
    "Defense +3":  (80, 0, 3)
}
#boss stats
with open("2015/Day21/boss_stat") as f:
    boss_health = int(f.readline().split(": ")[1])
    boss_dmg = int(f.readline().split(": ")[1])
    boss_armor = int(f.readline().split(": ")[1])



def isWin(d,a):
    player_health = 100
    boss_current_health = boss_health

    while player_health > 0 and boss_current_health > 0:
        boss_current_health -= max(1, d - boss_armor)
        if boss_current_health <=0:
            return True
        player_health -= max(1, boss_dmg - a)
    return False



#all combinations of 1 weapon, 0-1 armor, 0-2 rings
combs = product(list(weapons.keys()), list(armor.keys())+[None], list(rings.keys())+[None], list(rings.keys())+[None])
combined_dict = weapons | armor | rings

max_cost = None
for i in combs:
    if i[-1] == i[-2] and i[-1] != None:
        continue
    dmg = 0
    armor = 0
    cost = 0
    for j in i:
        if j == None:
            continue
        dmg += combined_dict[j][1]
        armor += combined_dict[j][2]
        cost += combined_dict[j][0]
    if not isWin(dmg, armor):
        if max_cost == None or cost > max_cost:
            max_cost = cost
    
print(max_cost)
