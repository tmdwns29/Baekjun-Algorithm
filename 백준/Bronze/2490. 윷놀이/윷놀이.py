import sys
input = sys.stdin.readline

for _ in range(3):
    JJak = list(map(int, input().split()))
    if JJak.count(0) == 1:
        print('A')
    elif JJak.count(0) == 2:
        print('B')
    elif JJak.count(0) == 3:
        print('C')
    elif JJak.count(0) == 4:
        print('D')
    elif JJak.count(1) == 4:
        print('E')