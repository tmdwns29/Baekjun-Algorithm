import sys
input = sys.stdin.readline

T = int(input())

for t in range(1, T+1):
    n = int(input())
    X = list(map(int, input().split()))
    Y = list(map(int, input().split()))

    X.sort(reverse=True)
    Y.sort()
    res = 0
    for i in range(n):
        res += X[i]*Y[i]
    print(f'Case #{t}: {res}')