with open('2015/Day8/test') as f:
    lines = f.read().splitlines()
    
num_endcoded_mem_chr = 0
num_original_mem_chr = 0
for s in lines:

    num_endcoded_mem_chr += len(s) + s.count('"') + s.count('\\') +2
    num_original_mem_chr += len(s)

print(num_endcoded_mem_chr - num_original_mem_chr)
