import hashlib
with open("2016/Day5/test") as f:
    door_id = f.read().strip()

password = ""
i = 0
while len(password) < 8:
    text = door_id + str(i)
    h = hashlib.md5(text.encode('utf-8')).hexdigest()
    if h.startswith("0"*5):
        password+= h[5]

    i+=1

print(password)