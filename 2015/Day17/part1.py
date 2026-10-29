from itertools import combinations
with open("2015/Day17/test") as f:
    lines = f.read().splitlines()
    ls=[]
    for line in lines:
        ls.append(int(line))
print(ls)
c=0
for i in range(2,len(ls)+1):
    for comb in combinations(ls,i):
        if sum(comb)==150:
            c+=1
print(c)