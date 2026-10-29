with open('2015/Day3/test') as file:
    inp = file.read()
pos = (0,0)
houses = set() #set of visited houses
houses.add(pos) #starting position
for move in inp:
    if move == '^':
        pos = (pos[0], pos[1]+1)
    elif move == 'v':
        pos = (pos[0], pos[1]-1)
    elif move == '<':
        pos = (pos[0]-1, pos[1])
    elif move == '>':
        pos = (pos[0]+1, pos[1])
    houses.add(pos)
print(len(houses))