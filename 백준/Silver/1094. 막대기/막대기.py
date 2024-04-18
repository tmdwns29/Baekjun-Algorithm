import sys, math
input = sys.stdin.readline

X = int(input())

arr = [64, 32, 16, 8, 4, 2, 1]
count = 0

for i in range(len(arr)):
    if X >= arr[i]:
        count += 1
        X -= arr[i]

    if X == 0:
        break
print(count)