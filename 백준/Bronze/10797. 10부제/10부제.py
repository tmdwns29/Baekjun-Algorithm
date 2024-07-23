import sys
input = sys.stdin.readline

N = input().rstrip()
nums = list(map(str, input().split()))
cnt = 0

for i in nums:
  if i[-1] == N:
    cnt += 1
print(cnt)