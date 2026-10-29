instructions = []
with open('2015/Day23/test') as f:
    lines = f.read().splitlines()
    for line in lines:
        instructions.append(line.replace(',', '').split())

registers = {'a': 1, 'b': 0}
i=0
while 0 <= i < len(instructions):
    ins = instructions[i]
    if ins[0] == 'hlf':
        registers[ins[1]] //= 2
    elif ins[0] == 'tpl':
        registers[ins[1]] *= 3
    elif ins[0] == 'inc':
        registers[ins[1]] += 1
    elif ins[0] == 'jmp':
        i += int(ins[1])
        continue
    elif ins[0] == 'jie':
        if registers[ins[1]] % 2 == 0:
            i += int(ins[2])
            continue
    elif ins[0] == 'jio':
        if registers[ins[1]] == 1:
            i += int(ins[2])
            continue
    i += 1

print(registers)