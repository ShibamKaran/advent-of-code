with open('2015/Day7/test') as f:
    lines = f.read().splitlines()
    wires = {}
    for line in lines:
        parts = line.split()
        inp = parts[:-2] #-> is at index -2
        if len(inp) == 1: # direct assignment
            #inp = inp[0]
            if inp[0].isdigit():
                inp = int(inp[0])
        elif len(inp) == 3: #index 0 and 2 to int if possible
            if inp[0].isdigit():
                inp[0] = int(inp[0])
            if inp[2].isdigit():
                inp[2] = int(inp[2])

        out = parts[-1]

        wires[out] = inp 

def replace_solved():
    for key,value in wires.items():
        
        #not needed but for clarity and will probably speed up a bit
        if isinstance(value, int): # already resolved
            continue

        if isinstance(value, list): # operation to be performed
            if len(value) == 1 and isinstance(value[0], int): #resolved and ready for assignment
                wires[key] = value[0]
            elif 'AND' in value or 'OR' in value:
                if isinstance(value[0], str): #not yet replaced
                    #replace with int if possible
                    if isinstance(wires[value[0]], int): 
                        value[0] = wires[value[0]]
                if isinstance(value[2], str):
                    #replace with int if possible
                    if isinstance(wires[value[2]], int):
                        value[2] = wires[value[2]]
            elif 'NOT' in value:
                if isinstance(value[1], str):
                    #replace with int if possible
                    if isinstance(wires[value[1]], int):
                        value[1] = wires[value[1]]
            else: #LSHIFT or RSHIFT or single wire assignment
                if isinstance(value[0], str):
                    #replace with int if possible
                    if isinstance(wires[value[0]], int):
                        value[0] = wires[value[0]]


def solve():
    for key,value in wires.items():
        #not needed but for clarity and will probably speed up a bit
        if isinstance(value, int): # already resolved
            continue
        if isinstance(value, list) and len(value) > 1: # operation to be performed
            if 'NOT' in value:
                if isinstance(value[1], int):
                    wires[key] = ~value[1] & 0xFFFF #16 bit mask
            else:
                if isinstance(value[0],int) and isinstance(value[2],int):
                    if 'AND' in value:
                        wires[key] = value[0] & value[2]
                    elif 'OR' in value:
                        wires[key] = value[0] | value[2]
                    elif 'LSHIFT' in value:
                        wires[key] = (value[0] << value[2]) & 0xFFFF #16 bit mask
                    elif 'RSHIFT' in value:
                        wires[key] = value[0] >> value[2]
                
while not isinstance(wires['a'], int):
    replace_solved()
    solve()
    
print(wires['a'])
