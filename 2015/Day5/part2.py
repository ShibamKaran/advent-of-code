with open('2015/Day5/test') as file:
    inp = file.read()
    inp = inp.splitlines()

nice_strs=[]
for s in inp:
    # Rule 1: It contains a pair of any two letters that appears at least twice
    #  in the string without overlapping
    for i in range(len(s)-1):
        pair = s[i] + s[i+1]
        if pair in s[i+2:]:
            break
    else:
        continue

    # Rule 2: It contains at least one letter which repeats with exactly one letter between them
    for i in range(len(s)-2):
        if s[i] == s[i+2]:
            nice_strs.append(s)
            break
    
print(len(nice_strs))