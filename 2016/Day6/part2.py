with open("2016/Day6/test") as f:
    lines = f.read().splitlines()

column = {}
for i in range(len(lines[0])):
    column[i] = []

for msg in lines:
    for i in range(len(msg)):
        column[i].append(msg[i])

ans = ""
for v in column.values():
    ans += min(v, key = v.count)
print(ans)
    