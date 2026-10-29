with open('2015/Day1/test') as file:
    inp = file.read()

floor = 0
for i in inp:
    if i == '(':
        floor += 1
    elif i == ')':
        floor -= 1
print(floor)