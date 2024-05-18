import sys
input = sys.stdin.readline

N,M = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(N)]

M,K = map(int, input().split())
B = [list(map(int, input().split())) for _ in range(M)]

result = [[0]*K for _ in range(N)]

for i in range(N):
    for j in range(K):
        for k in range(M):
            result[i][j] += A[i][k] * B[k][j]

for arr in result:
    print(*arr)