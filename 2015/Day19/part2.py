import random

med = open("2015/Day19/molecule").read().strip()
with open("2015/Day19/test") as f:
    lines = f.read().splitlines()

# IMPORTANT: list, not dict
replacements = []
for line in lines:
    v, k = line.split(" => ")
    replacements.append((k, v))

# longest first
replacements.sort(key=lambda item: -len(item[0]))

def steps_counter(med):
    global replacements
    target = med

    while True:
        med = target
        steps = 0

        shuffled = replacements[:]
        random.shuffle(shuffled)

        while med != "e":
            found = False
            for k, v in shuffled:
                if k in med:
                    med = med.replace(k, v, 1)
                    steps += 1
                    found = True
                    break

            if not found:
                break   # dead end → restart

        if med == "e":
            return steps

print(steps_counter(med))
#SEEEE LATERR
