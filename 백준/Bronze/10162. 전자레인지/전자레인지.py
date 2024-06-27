import sys
input = sys.stdin.readline

T = int(input())
a,b,c = 0,0,0

while T > 0:
    if T >= 300:
        a = T // 300
        T %= 300
    elif 60 <= T < 300:
        b = T // 60
        T %= 60
    elif 1<= T < 60:
        if T % 10 != 0:
            print(-1)
            exit(0)
        c = T // 10
        T %= 10
print(a,b,c)