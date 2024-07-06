import sys
input = sys.stdin.readline

N = int(input())
cnt = 0

while N > 0:
    if N % 3 == 0:
        N -= 3
    else:
        N -= 1
    cnt += 1
if cnt % 2 == 1:
    print('SK')
else:
    print('CY')