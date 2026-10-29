with open('2015/Day4/test') as file:
    inp = file.read()


import hashlib

# Compute MD5 hash
i=0
ans = ''
while True:
    ans = inp + str(i)
    md5_hash = hashlib.md5(ans.encode()).hexdigest()
    if md5_hash.startswith('00000'): #5 leading zeroes
        break
    else:
        i += 1

print(i)
