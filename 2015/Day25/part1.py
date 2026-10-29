with open("2015/Day25/test") as f:
    inp = f.read().splitlines()
    ROW = int(inp[0].split()[-1])
    COLUMN = int(inp[1].split()[-1])


i=1
j=1
value = 20151125
while i != ROW or j != COLUMN:
    if i == 1:
        i = j + 1
        j = 1
    else:
        i -= 1
        j += 1
    value = (value * 252533) % 33554393

print(value)