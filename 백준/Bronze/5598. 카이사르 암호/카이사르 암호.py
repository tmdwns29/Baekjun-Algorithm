caesar = input().rstrip()
result = ''
for i in caesar:
    if ord(i) <= 67:
        result += chr(ord(i)+23)
        continue
    result += chr(ord(i)-3)
print(result)