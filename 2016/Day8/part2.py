with open("2016/Day8/test") as f:
    lines = f.read().splitlines()
    data = []
    for line in lines:
        line = line.split()
        if "rect" in line:
            A, B = line[1].split("x")
            data.append(["rect", int(A), int(B)])
        else: #rotate
            A = line[2].split("=")[-1]
            B = line[4]
            data.append(["rotate", line[1], int(A), int(B)])
print(data)
screen = []
for i in range(6):
    screen.append([])
    for j in range(50):
        screen[i].append(".")

def rect(A,B):
    global screen
    for i in range(B):
        for j in range(A):
            screen[i][j] = "#"

def rotate_row(A,B):
    global screen
    screen[A] = screen[A][-B:] + screen[A][:-B]

def rotate_col(A,B):
    global screen
    col = []

    for r in range(len(screen)):
        col.append(screen[r][A])

    col = col[-B:] + col[:-B]

    for i in range(len(col)): 
        screen[i][A] = col[i]

for cmd in data:
    if cmd[0] == "rect":
        rect(cmd[1], cmd[2])
    elif cmd[0] == "rotate":
        if cmd[1] == "row":
            rotate_row(cmd[2], cmd[3])
        else:
            rotate_col(cmd[2], cmd[3])

    for i in screen:
        print("".join(i).replace(".", " ").replace("#", "█"))
    print()

s = 0
for i in screen:
    s += i.count("#")
print(s)