N = int(input())
arr, res, find = [], [], True
start = 1
for _ in range(N):
    num = int(input())

    while start <= num:
        arr.append(start)
        res.append('+')
        start += 1

    if arr[-1] == num:
        arr.pop()
        res.append('-')

    else:
        find = False
        break

if not find:
    print('NO')
else:
    for i in res:
        print(i)