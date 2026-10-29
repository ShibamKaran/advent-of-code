with open('2015/Day3/test') as file:
    inp = file.read()
santa_pos = (0,0)
robo_pos = (0,0)
houses = set() #set of visited houses
houses.add(santa_pos) #starting position
turn = 0 #0 for santa, 1 for robo
for move in inp:
    if turn == 0:
        pos = santa_pos
    else:
        pos = robo_pos
    if move == '^':
        pos = (pos[0], pos[1]+1)
    elif move == 'v':
        pos = (pos[0], pos[1]-1)
    elif move == '<':
        pos = (pos[0]-1, pos[1])
    elif move == '>':
        pos = (pos[0]+1, pos[1])
    houses.add(pos)

    if turn == 0:
        santa_pos = pos
        turn = 1
    else:
        robo_pos = pos
        turn = 0
    
print(len(houses))
