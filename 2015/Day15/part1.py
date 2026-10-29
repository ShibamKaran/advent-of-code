# capacity, durability, flavor, texture, calories
with open("2015/Day15/test") as f:
    lines = f.readlines()
    name = []
    rest = []
    for i in range(len(lines)):
        name.append(lines[i].split(":")[0])
        rest.append(lines[i].split(":")[1].strip().split(","))
    d={}
    for i in range(len(name)):
        d[name[i]] = (int(rest[i][0].split()[1]), int(rest[i][1].split()[1]), int(rest[i][2].split()[1]), int(rest[i][3].split()[1]), int(rest[i][4].split()[1]))


ls=[]
for i in range(101):
    for j in range(101-i):
        for k in range(101-j-i):
            l = 100 - i - j - k
            if l>=0:
                ls.append((i,j,k,l))

max_score = 0
for i in range(len(ls)):
    cap = d['Sprinkles'][0]*ls[i][0] + d['Butterscotch'][0]*ls[i][1] + d['Chocolate'][0]*ls[i][2] + d['Candy'][0]*ls[i][3]
    dur = d['Sprinkles'][1]*ls[i][0] + d['Butterscotch'][1]*ls[i][1] + d['Chocolate'][1]*ls[i][2] + d['Candy'][1]*ls[i][3]
    fla = d['Sprinkles'][2]*ls[i][0] + d['Butterscotch'][2]*ls[i][1] + d['Chocolate'][2]*ls[i][2] + d['Candy'][2]*ls[i][3]
    tex = d['Sprinkles'][3]*ls[i][0] + d['Butterscotch'][3]*ls[i][1] + d['Chocolate'][3]*ls[i][2] + d['Candy'][3]*ls[i][3]
    if cap<0:
        cap=0
    if dur<0:
        dur=0
    if fla<0:
        fla=0
    if tex<0:
        tex=0
    score = cap * dur * fla * tex
    max_score = max(max_score, score)
print(max_score)