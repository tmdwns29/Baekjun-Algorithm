import sys
input = sys.stdin.readline

sum_ = 0
nums = []

for i in range(7):
    num = int(input())
    if num % 2 == 1:
        nums.append(num)
if not nums: print(-1)
else:
    print(sum(nums))
    print(min(nums))