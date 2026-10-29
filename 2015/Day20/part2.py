def elf_num(n): #factors of house no
    fac = set()
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            fac.add(i)
            fac.add(n // i)
    return fac

with open("2015/Day20/test") as f:
    inp = int(f.read().strip())
house = 1
elfs_delivery = {}
while True:
    elfs = elf_num(house)
    for elf in elfs.copy():
        if elf in elfs_delivery:
            if elfs_delivery[elf] >= 50:
                elfs.remove(elf)
            else:
                elfs_delivery[elf] += 1
        else:
            elfs_delivery[elf] = 1
    present = sum(elfs) * 11
    if present >= inp:
        print(house)
        break
    house += 1