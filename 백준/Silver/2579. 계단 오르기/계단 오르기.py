import sys
input = sys.stdin.readline

N = int(input())

step = [0]*301
for i in range(1, N+1):
    step[i] = int(input())

dp = [0]*301
dp[1] = step[1]
dp[2] = step[1] + step[2]
dp[3] = max(step[1], step[2]) + step[3]

for i in range(4, N+1):
    dp[i] = max(dp[i-3]+step[i-1]+step[i], dp[i-2]+step[i])

print(dp[N])