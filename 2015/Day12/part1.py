with open('2015/Day12/test') as f:
    s=f.read()

s=s+" "
n=0
sum=0
sign=1
for ch in s:
    if ch=='-':
        sign=-1

    if ch.isdigit():
        n=n*10+int(ch)
    elif n!=0:
        sum=sum+(int(n) * sign)
        n=0
        sign=1

print(sum)

