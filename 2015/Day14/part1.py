with open('2015/Day14/test') as f:
    lines = f.read().splitlines()
    d={}
    for line in lines:
        ls=line.split()
        name = ls[0]
        speed = int(ls[3])
        duration = int(ls[6])
        rest = int(ls[-2])
        d[name] = [speed, duration, rest] 

t= 2503
def get_distance(name):
    i=0
    distance = 0
    speed, duration, rest = d[name]
    move_rest = 1 # 1 for moving, 0 for resting
    while i < t:
        if move_rest == 1:
            if i + duration <= t:
                distance += speed * duration
                i += duration
            else:
                distance += speed * (t - i)
                i = t
            move_rest = 0
        else:
            if i + rest <= t:
                i += rest
            else:
                i = t
            move_rest = 1
    return distance

max_distance = 0
for name in d.keys():
    dist = get_distance(name)
    if dist > max_distance:
        max_distance = dist
print(max_distance)
        

    



