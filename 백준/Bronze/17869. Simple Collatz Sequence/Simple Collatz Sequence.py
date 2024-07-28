import sys
input = sys.stdin.readline

S = int(input())
cnt = 0
while S != 1:
    if S % 2 == 0:
        S //= 2
    else:
        S += 1
    cnt += 1

print(cnt)