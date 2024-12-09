caesar = input().rstrip()
result = ''

for i in caesar:
    if 65<=ord(i)<=90:
        if ord(i)+13 > 90:
            result += chr(ord(i)-13)
            continue
        result += chr(ord(i)+13)
    elif 97<=ord(i)<=122:
        if ord(i)+13 > 122:
            result += chr(ord(i)-13)
            continue
        result += chr(ord(i)+13)
    else:
        result += i
print(result)