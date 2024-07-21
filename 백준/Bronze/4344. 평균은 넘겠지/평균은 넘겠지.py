import sys
input = sys.stdin.readline

C = int(input())

for _ in range(C):
    N = list(map(int, input().split()))
    cnt = 0

    for i in range(1, N[0]+1):
        if (sum(N[1:]) / N[0]) < N[i]:
            cnt += 1
    print('%.3f%%'%((cnt / N[0])*100))