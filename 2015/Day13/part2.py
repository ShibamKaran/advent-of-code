from itertools import permutations

with open('2015/Day13/test') as f:
    lines = f.read().splitlines()
    d={}
    names = set()
    for i in range(len(lines)):
        ls = lines[i].split()
        sign=1
        if 'lose' in ls:
            sign=-1
        #lines[i] = [ls[0],ls[-1][:-1],int(ls[3])*sign]
        d[(ls[0],ls[-1][:-1])] = int(ls[3])*sign
        names.add(ls[0])

names.add('Me')

optimal_happiness = None
for arrangement in permutations(names):
    total_happiness = 0
    for i in range(len(arrangement)):
        current = arrangement[i]
        if current == 'Me':
            continue
        left = arrangement[i-1]
        if i == len(arrangement)-1:
            right = arrangement[0]
        else:
            right = arrangement[i+1]
        if left != 'Me':
            total_happiness += d[(current, left)]
        if right != 'Me':
            total_happiness += d[(current, right)]
    if optimal_happiness is None or total_happiness > optimal_happiness:
        optimal_happiness = total_happiness

print(optimal_happiness)