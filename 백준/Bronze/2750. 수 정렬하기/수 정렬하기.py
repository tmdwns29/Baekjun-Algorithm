import sys
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
for i in sorted(arr):
    print(i)