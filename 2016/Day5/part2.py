import hashlib
with open("2016/Day5/test") as f:
    door_id = f.read().strip()

door_id = door_id.encode('utf-8')
password = ["_"] * 8
i = 0
while "_" in password:
    text = door_id + str(i).encode('utf-8')
    d = hashlib.md5(text).digest()
    if d[0] == 0 and d[1] == 0 and d[2] < 16:
        h = hashlib.md5(text).hexdigest()
        pos = h[5]
        val = h[6]
        if pos.isdigit():
            pos = int(pos)
            if pos <= 7 and password[pos] == "_": 
                password[pos] = val
    i+=1
print("".join(password))
