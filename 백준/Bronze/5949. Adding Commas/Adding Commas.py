N = list(input().rstrip())
res = ''
cnt = 1

for n in N[-1::-1]:
    res += n
    if cnt % 3 == 0 and cnt != len(N):
        res += ','
    cnt += 1
print(res[-1::-1])