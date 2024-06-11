import sys
input = sys.stdin.readline

N = int(input())
size = list(map(int, input().split()))
T, P = map(int, input().split())
tshirt, pen = 0,0
pen = N // P

for i in size:
    if i % T == 0:
        tshirt += i//T
    else:
        tshirt += i//T + 1
print(tshirt)
print(pen, N-(pen*P))