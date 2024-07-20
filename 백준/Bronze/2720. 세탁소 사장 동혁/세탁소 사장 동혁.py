import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    C = int(input())
    change = [0, 0, 0, 0]

    while C != 0:
        if C >= 25:
            change[0] += C // 25
            C %= 25
        elif 10 <= C < 25:
            change[1] += C // 10
            C %= 10
        elif 5 <= C < 10:
            change[2] += C // 5
            C %= 5
        else:
            change[3] += C
            C = 0
    print(*change)