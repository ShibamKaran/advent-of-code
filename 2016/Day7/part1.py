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

def check_abba(s):
    for i in range(len(s) - 3):
        if s[i: i+2] == s[i+2: i+4][::-1] and s[i] != s[i+1]:
            return True
    return False

c=0
for i in data:
    for j in i[1]:
        if check_abba(j):
            break
    else:
        for j in i[0]:
            if check_abba(j):
                c+=1
                break
print(c)