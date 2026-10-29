with open('2015/Day5/test') as file:
    inp = file.read()
    inp = inp.splitlines()

nice_strs=[]
for s in inp:
    # Rule 1: It contains at least three vowels (aeiou only)
    vc=0
    for ch in s:
        if ch in 'aeiou':
            vc+=1
    if vc<3:
        continue
    
    # Rule 2: It contains at least one letter that appears twice in a row
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            break
    else:
        continue

    # Rule 3: It does not contain the strings ab, cd, pq, or xy
    forbidden = ['ab', 'cd', 'pq', 'xy']
    for fb in forbidden:
        if fb in s:
            break
    else:
        nice_strs.append(s) #add only if all 3 rules are satisfied

print(len(nice_strs))
        