import sys
input = sys.stdin.readline

A,B = map(int, input().split())

nums = []
for i in range(1, 1001):
    for _ in range(i):
        if len(nums) == B:
            break
        nums.append(i)

print(sum(nums[A-1:B]))