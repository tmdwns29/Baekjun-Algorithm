N = int(input())
cnt=0
i = 1
while N > 0:
    if N < i:
        i = 1
    N -= i
    i += 1
    cnt += 1

print(cnt)