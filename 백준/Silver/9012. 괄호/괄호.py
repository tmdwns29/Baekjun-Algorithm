T = int(input())
count = 0

for i in range(T):
    vps = input()
    for j in vps:
        if count < 0: break
        elif j == '(': count += 1
        elif j == ')': count -= 1
    if count == 0: print('YES')
    else: print('NO')
    count = 0