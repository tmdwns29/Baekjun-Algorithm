import sys
input = sys.stdin.readline

N, M =map(int, input().split())
candy = []
dp = [[0]*(M+1) for _ in range(N+1)]

for _ in range(N):
    temp = list(map(int, input().split()))
    candy.append(temp)

for i in range(1, N+1):
    for j in range(1, M+1):
        dp[i][j] = max(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + candy[i-1][j-1]

print(dp[-1][-1])