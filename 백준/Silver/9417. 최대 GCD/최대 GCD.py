import sys, math
input = sys.stdin.readline

N = int(input())

for _ in range(N):
    nums = list(map(int, input().split()))
    max_gcd = 0
    for i in range(len(nums)): # 0 1 2 3
        for j in range(i, len(nums)): # 0 1 2 3
            if j != i:
                n = math.gcd(nums[i], nums[j])
                if n > max_gcd:
                    max_gcd = n
    print(max_gcd)