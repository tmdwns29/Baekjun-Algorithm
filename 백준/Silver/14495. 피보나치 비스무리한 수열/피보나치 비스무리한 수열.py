import sys
input = sys.stdin.readline

N = int(input())

dp = [0]*117
dp[1] = 1
dp[2] = 1
dp[3] = 1

for i in range(3, N+1):
    dp[i] = dp[i-1]+dp[i-3]

print(dp[N])