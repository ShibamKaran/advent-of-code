with open('2015/Day8/test') as f:
    lines = f.read().splitlines()
    
num_code_chr = 0
num_mem_chr = 0
for s in lines:
    num_code_chr += len(s)
    num_mem_chr += len(eval(s))

print(num_code_chr - num_mem_chr)
