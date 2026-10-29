with open("2015/Day10/test") as f:
    seq = f.read().strip()
for t in range(50):
    seq = seq+' '
    new_seq = ''
    count = 1
    for i in range(len(seq)-1):
        if seq[i] == seq[i+1]:
            count += 1
        else:
            new_seq += str(count) + seq[i]
            count = 1
    seq = new_seq
    print(t,len(seq))

print(len(seq))

