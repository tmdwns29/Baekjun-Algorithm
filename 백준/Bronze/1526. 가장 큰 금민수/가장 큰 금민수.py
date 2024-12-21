N = int(input())

while True:
    flag = True
    for n in str(N): # 77
        if n != '4' and n != '7':
            flag = False
            break
    if flag:
        break
    N -= 1
print(N)