import sys, heapq 
input = sys.stdin.readline

N = int(input())
arr = []

for i in range(N):
    x = int(input())
    x *= -1
    if x == 0:
        if arr:
            sys.stdout.write("%d\n"%(-1*(heapq.heappop(arr))))
        else:
            sys.stdout.write("%d\n"%0)
    else:
        heapq.heappush(arr, x)