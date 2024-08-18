import sys
input = sys.stdin.readline

P, N = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
i, cnt = 0,0

while i < N:
    if P < 200:
        P += nums[i]
    else:
        break
    cnt += 1
    i += 1
print(cnt)