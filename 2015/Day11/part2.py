
password = input("Part 1 answer: ")

def is_valid():
    global password
    #doesnt contain i,o,l
    if 'i' in password or 'o' in password or 'l' in password:
        return False
    
    #contains increasing straight of 3 letters
    for i in range(len(password)-2):
        if ord(password[i]) == (ord(password[i+1]) - 1) == (ord(password[i+2]) - 2):
            break
    else:
        return False
    
    #contains two different non-overlapping pairs
    pair_count = 0
    i=0
    while i<len(password)-1:
        if password[i]==password[i+1]:
            pair_count += 1
            i += 2
        else:
            i += 1
    
    if pair_count < 2:
        return False
    
    return True



def increment_password():
    global password
    password_list = list(password)
    i = len(password_list) - 1
    carry = 1
    while i >= 0 and carry:
        if password_list[i] == 'z':
            password_list[i] = 'a'
            carry = 1
        else:
            password_list[i] = chr(ord(password_list[i]) + 1)
            carry = 0
        i -= 1
    password = ''.join(password_list)


#Next password
increment_password()
while is_valid() == False:
    increment_password()
print(password)


