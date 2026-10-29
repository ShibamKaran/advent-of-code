with open("2016/Day9/test") as f:
    data = f.read()

decomp = ""
i = 0
while i < len(data):
    a = data.index("(", i)

    decomp += data[i:a]

    b = data.index(")", a)

    l, r = data[a+1:b].split("x")
    l, r = int(l), int(r)

    decomp += data[b+1: b+l+1] * r

    i = b + l + 1

print(len(decomp))
