import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []

for i in range(N):
    x = int(input())
    if x == 0:
        if len(heap) == 0:
            out = 0
        else:
            out = heapq.heappop(heap)
        print(out)
    else:
        heapq.heappush(heap, x)