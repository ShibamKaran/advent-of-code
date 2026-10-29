with open('2015/Day12/test') as f:
    s=f.read()

d=eval(s)

def remove_red(o):
    if isinstance(o, list):
        #print("list        ",o)
        for i in o:
            remove_red(i)

    if isinstance(o, dict):
        for k,v in list(o.items()):
            if v=="red" or k=="red":
                #print("removing      ",o)
                o.clear()
            if isinstance(v, list):
                for i in v:
                    #print("dict list       ",i)
                    remove_red(i)
            if isinstance(v, dict):
                #print("dict dict      ",v)
                remove_red(v)

remove_red(d)

s=str(d)+" "
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




