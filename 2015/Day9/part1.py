from itertools import permutations

with open('2015/Day9/test') as f:
    lines = f.read().splitlines()
    dist={}
    towns=set()
    for line in lines:
        l, d = line.split(' = ')
        d=int(d)
        t1,t2 = l.split(' to ')
        dist[(t1,t2)]=d
        dist[(t2,t1)]=d
        towns.add(t1)
        towns.add(t2)

shortest_dist = None
for route in permutations(towns):
    route_dist = 0
    for i in range(len(route)-1):
        route_dist += dist[(route[i], route[i+1])]

    if shortest_dist is None or route_dist < shortest_dist:
        shortest_dist = route_dist

print(shortest_dist)
