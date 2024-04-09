import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*50001
dp[1] = 1
for i in range(2, N+1):
    min_ = 4
    j = 1
    while j**2 <= i:
        min_ = min(min_, dp[i-j**2])
        j += 1
    dp[i] = min_ + 1
print(dp[N])