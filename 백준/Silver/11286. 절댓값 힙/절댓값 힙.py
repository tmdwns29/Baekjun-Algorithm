import sys, heapq
input = sys.stdin.readline
print = sys.stdout.write

arr = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(arr, (abs(x), x))
    else:
        if arr:
            print("%d\n"%heapq.heappop(arr)[1])
        else:
            print("%d\n"%0)