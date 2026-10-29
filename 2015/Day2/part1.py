with open('2015/Day2/test') as file:
    inp = file.read()
    inp = inp.splitlines()
    for i in range(len(inp)):
        inp[i] = inp[i].split('x')

ans=0
for l,w,h in inp:
    l = int(l)
    w = int(w)
    h = int(h)
    side1 = l*w
    side2 = w*h
    side3 = h*l
    smallest = min(side1, side2, side3)
    sf = 2*side1 + 2*side2 + 2*side3
    total = sf + smallest #surface area + smallest side
    ans += total

print(ans)