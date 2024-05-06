import sys
input = sys.stdin.readline

N = int(input())

dp = [0]*100001
dp[1] = 3 # 0(1)+1(2) = 3
dp[2] = 7 # 0(1)+1(4)+2(2) = 7

for i in range(3, N+1):
    dp[i] = (dp[i-2]+(2*dp[i-1]))%9901
print(dp[N]%9901)