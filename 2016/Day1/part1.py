with open('2016/Day1/test') as f:
    ins=f.read().split(', ')
x,y = 0,0
dir = {'N':(0,1),'W':(-1,0),'S':(0,-1),'E':(1,0)}
dirs = ['N','W','S','E']
facing = 0
for i in ins:
    if i[0] == 'L':
        if facing == 0:
            facing = 3
        else:
            facing -= 1
    elif i[0] == 'R':
        if facing == 3:
            facing = 0
        else:
            facing += 1
    steps = int(i[1:])
    x += steps * dir[dirs[facing]][0]
    y += steps * dir[dirs[facing]][1]
print(abs(x)+abs(y))