with open('2015/Day1/test') as file:
    inp = file.read()

floor = 0
for i in range(len(inp)):
    if inp[i] == '(':
        floor += 1
    elif inp[i] == ')':
        floor -= 1
    if floor == -1:
        print(i + 1) #as indexing starts from 1
        break
