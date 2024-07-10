S = input()
alphabet = [0]*26
for c in S:
    alphabet[ord(c)-97] += 1
print(*alphabet)