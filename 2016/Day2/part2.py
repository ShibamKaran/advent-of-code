with open('2016/Day2/test') as f:
    instructions = f.read().splitlines()
numpad = [[0, 0, 1, 0, 0],
          [0, 2, 3, 4, 0],
          [5, 6, 7, 8, 9],
          [0,'A', 'B', 'C',0],
          [0, 0,'D', 0, 0]]

x, y = 0, 2
code = ''

for i in instructions:
    for cmd in i:
        t_x, t_y = x, y
        if cmd == 'U' and t_y > 0:
            t_y-=1
        elif cmd == 'D' and t_y < 4:
            t_y+=1
        elif cmd == 'L' and t_x > 0:
            t_x-=1
        elif cmd == 'R' and t_x < 4:
            t_x+=1

        if numpad[t_y][t_x] != 0:
            x, y = t_x, t_y
        

    code += str(numpad[y][x])

print(code)