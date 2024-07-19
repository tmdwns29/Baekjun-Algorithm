import sys
input = sys.stdin.readline

n, d = map(int, input().split())
d = str(d)
cnt = 0

digit = [str(i) for i in range(1, n+1)]

for i in digit:
    if len(i) == 1 and i == d:
        cnt += 1
    else:
        for j in range(len(i)):
            if i[j] == d:
                cnt += 1
print(cnt)