ciphertext = 'afZ_r9VYfScOeO_UL^RWUc'
j = 5
for i in ciphertext:
    print(chr(ord(i) + j), end='')
    j += 1
