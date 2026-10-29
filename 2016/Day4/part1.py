def get_top5(freq):
    sorted_keys = sorted(freq.keys(), key=freq.get, reverse=True)    
    same_val = {}
    for i in range(len(sorted_keys)):
        if freq[sorted_keys[i]] not in same_val:
            same_val[freq[sorted_keys[i]]] = []
        same_val[freq[sorted_keys[i]]].append(sorted_keys[i])

    s = ""
    for v in same_val.values():
        s += "".join(sorted(v))
    return s[:5]
    


with open('2016/Day4/test') as f:
    lines = f.read().splitlines()
    data = []
    for line in lines:
        data.append( ( line[:line.rindex('-')] , 
                      int(line[line.rindex('-')+1 : line.rindex('[')]) ,
                      line[line.rindex('[')+1 : line.rindex(']')]))

sector_real_rooms = []
for room in data:
    name, sector, checksum = room
    name = name.replace('-','')
    freq = {}
    for ch in name:
        if ch not in freq:
            freq[ch] = 0
        freq[ch] += 1
    real_checksum = get_top5(freq.copy())
    if real_checksum == checksum:
        sector_real_rooms.append(sector)

print("Sum of sector IDs of real rooms: ", sum(sector_real_rooms))
    
    


    
    