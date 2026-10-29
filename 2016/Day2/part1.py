with open('2016/Day2/test') as f:
    instructions = f.read().splitlines()
numpad = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]
x, y = 1, 1
code = ''

for i in instructions:
    for cmd in i:
        if cmd == 'U' and y > 0:
            y-=1
        elif cmd == 'D' and y < 2:
            y+=1
        elif cmd == 'L' and x > 0:
            x-=1
        elif cmd == 'R' and x < 2:
            x+=1
    code += str(numpad[y][x])

print(code)