import sys
input = sys.stdin.readline

arr = list(map(int, input().split()))
print(*sorted(arr))