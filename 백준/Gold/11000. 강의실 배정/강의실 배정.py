import sys, heapq
input = sys.stdin.readline

N = int(input())
table = []

for _ in range(N):
    S, T = map(int, input().split())
    table.append((S,T))

table.sort(key=lambda x: (x[0],x[1]))
result = [table[0][1]]

for i in range(1, N):
    if result[0] <= table[i][0]:
        heapq.heappop(result)
    heapq.heappush(result, table[i][1])

print(len(result))