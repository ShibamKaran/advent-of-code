with open('2015/Day6/test') as file:
    inp = file.read()
    inp = inp.splitlines()
    #processing input to required format
    for i in range(len(inp)):
        inp[i] = inp[i].split()
        #removing unnecessary elements
        if len(inp[i])==5: 
            inp[i].pop(0)
        inp[i].pop(2) #remove through

        inp[i][1] = inp[i][1].split(',')
        inp[i][1][0], inp[i][1][1] = int(inp[i][1][0]), int(inp[i][1][1])

        inp[i][2] = inp[i][2].split(',')
        inp[i][2][0], inp[i][2][1] = int(inp[i][2][0]), int(inp[i][2][1])


ls = []
for i in range(1000):
    ls.append([0]*1000)


for inst in inp:
    for x in range(inst[1][0],inst[2][0]+1):
        for y in range(inst[1][1],inst[2][1]+1):
            if inst[0]=='on':
                ls[x][y] += 1
            elif inst[0]=='off':
                if ls[x][y]>0:
                    ls[x][y] -= 1
            elif inst[0]=='toggle':
                ls[x][y] += 2

ans = 0
for row in ls:
    ans += sum(row)
print(ans)