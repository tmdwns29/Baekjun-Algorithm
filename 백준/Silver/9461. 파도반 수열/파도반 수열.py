import sys
input = sys.stdin.readline

T = int(input())
dp = [0]*101
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(T):
    N = int(input())
    for j in range(4, N+1):
        dp[j] = dp[j-2] + dp[j-3]
    print(dp[N])