with open('2015/Day16/test') as f:
    lines = f.read().splitlines()
    ls=[]
    #sue 1 to sue 500... add 1 to index
    for line in lines:
        wrds=line.split()
        t_dict={}
        t_dict[wrds[2][:-1]] = int(wrds[3][:-1])
        t_dict[wrds[4][:-1]] = int(wrds[5][:-1])
        t_dict[wrds[6][:-1]] = int(wrds[7])
        ls.append(t_dict)

        
sue_stats = {
    "children": 3,
    "cats": 7,
    "samoyeds": 2,
    "pomeranians": 3,
    "akitas": 0,
    "vizslas": 0,
    "goldfish": 5,
    "trees": 3,
    "cars": 2,
    "perfumes": 1
}

for i in range(len(ls)):
    match = False
    for k,v in ls[i].items():
        if sue_stats[k] != v:
            break
    else:
        match = True
    if match:
        print("Sue", i+1)
        break
    