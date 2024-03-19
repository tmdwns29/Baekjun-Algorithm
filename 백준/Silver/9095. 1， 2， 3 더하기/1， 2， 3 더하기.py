import sys
input = sys.stdin.readline

T = int(input())
dp = [0,1,2,4]
for i in range(4, 11):
    dp.append(dp[i-3]+dp[i-2]+dp[i-1])

for _ in range(T):
    num = int(input())
    print(dp[num])