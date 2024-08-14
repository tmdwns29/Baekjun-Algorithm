import sys
input = sys.stdin.readline

players = []
name = []

N = int(input())
for _ in range(N):
    temp = list(map(int, input().split()))
    players.append(temp)
    if (17 in temp) or (18 in temp):
        if (17 in temp) and (18 in temp):
            name.append('both')
            continue
        if 17 in temp:
            name.append('zack')
        elif 18 in temp:
            name.append('mack')
    else:
        name.append('none')

for i in range(N):
    print(*players[i])
    print(name[i])
    print()