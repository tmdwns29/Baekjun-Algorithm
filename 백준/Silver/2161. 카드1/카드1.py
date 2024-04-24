from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
arr = deque([i for i in range(1, N+1)])

while arr:
    print(arr.popleft(), end=' ')
    if arr:
        n = arr.popleft()
        arr.append(n)