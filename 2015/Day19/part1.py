med = open("2015/Day19/molecule").read().strip()
ls=[]
wrd = ""
for i in range(len(med)):
    if med[i].isupper():  # Check if the character is uppercase
        if wrd != "":
            ls.append(wrd)  # Append the current word to the list
        wrd = med[i]  # Start a new word
    else:
        wrd += med[i]  # Append the lowercase character to the current word

# Append the last word to the list
if wrd != "":
    ls.append(wrd)

with open("2015/Day19/test") as f:
    lines = f.read().splitlines()
    replacements = {}
    for line in lines:
        k, v = line.split(" => ")
        if k in replacements.keys():
            replacements[k].append(v)
        else:
            replacements[k] = [v]
mol_c = set()
for i in range(len(ls)):
    if ls[i] not in replacements.keys():
        continue
    for repl in replacements[ls[i]]:
        new_mol = "".join(ls[:i]) + repl + "".join(ls[i + 1 :])
        mol_c.add(new_mol)
print(len(mol_c))
