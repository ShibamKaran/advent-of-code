with open("2016/Day7/test") as f:
    lines = f.read().splitlines()
    data = []
    for line in lines:
        outer = []
        inner = []
        line = line.split("[")
        for i in line:
            if "]" in i:
                inner.append(i[:i.index("]")])
                outer.append(i[i.index("]")+1:])
            else:
                outer.append(i)
        data.append([outer, inner])

def check_aba(s):
    for i in range(len(s) - 2):
        if s[i] == s[i+2] and s[i] != s[i+1]:
            yield s[i:i+3] 

def convert_bab(s):
    s = s[1] + s[0] + s[1]
    return s

c=0
for i in data:
    outer_aba = []
    for j in i[0]:
        for k in check_aba(j):
            outer_aba.append(k)
    
    for j in outer_aba:
        f = False
        t = convert_bab(j)
        for k in i[1]:
            if t in k:
                c += 1
                f = True
                break
        if f:
            break
print(c)
