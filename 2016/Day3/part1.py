with open('2016/Day3/test') as f:
    data = f.read().splitlines()
    d = []
    for line in data:
        s1, s2, s3 = line.split()
        d.append((int(s1), int(s2), int(s3)))

valid_triangles = []
for i in d:
    s, m, l = sorted(i)
    if (s + m) > l:
        valid_triangles.append(i)
print(len(valid_triangles))
