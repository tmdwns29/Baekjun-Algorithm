import sys

T = int(sys.stdin.readline())
result = 0

for _ in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    arr = [[0]*(n+1) for _ in range(k+1)]

    for i in range(k + 1):
        for j in range(1, n + 1):
            if i == 0:
                arr[0][j] = j
            else:
                arr[i][j] = sum(arr[i - 1][1 : j + 1])

    print(arr[k][n])