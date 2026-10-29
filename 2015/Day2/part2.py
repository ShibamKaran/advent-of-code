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
    dimensions = [l, w, h]
    dimensions.sort()
    smallest_prem = 2*dimensions[0] + 2*dimensions[1]
    bow = l*w*h
    total = smallest_prem + bow
    ans += total

print(ans)