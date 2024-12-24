import sys
input = sys.stdin.readline

N = int(input())

dp = [0] * 36
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 5

for n in range(4, N+1):
    if n % 2 == 0:
        for i in range(0, n//2): # 2=0 4=1 6=2 8=3
            dp[n] += (dp[i]*(2*dp[n-i-1]))
    else:
        for j in range(0, n//2): # 3=0, 5=1, 7=2 | 3=1, 5=2, 7=3
            dp[n] += (dp[j]*(2*dp[n-j-1]))
        dp[n] += dp[j+1]**2
print(dp[N])