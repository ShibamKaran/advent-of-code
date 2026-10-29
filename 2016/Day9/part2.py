with open("2016/Day9/test") as f:
    data = f.read()

def get_decomp_len(start, end):
    a = data.find("(", start, end)
    if a == -1:
        return end - start
    b = data.find(")", a, end)
    l,r = data[a+1:b].split("x")
    l,r = int(l), int(r)
    left = r * get_decomp_len(b+1, b+l+1)
    right = get_decomp_len(b+l+1, end)
    return left + right

print(get_decomp_len(0, len(data)))  