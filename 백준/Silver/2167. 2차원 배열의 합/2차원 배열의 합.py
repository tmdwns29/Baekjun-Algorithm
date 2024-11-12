import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = []
for _ in range(N):
    temp = list(map(int, input().split()))
    arr.append(temp)
K = int(input())
for _ in range(K):
    i, j, x, y = map(int, input().split())
    sum_ = 0
    for a in range(i-1, x):
        for b in range(j-1, y):
            sum_ += arr[a][b]
    print(sum_)