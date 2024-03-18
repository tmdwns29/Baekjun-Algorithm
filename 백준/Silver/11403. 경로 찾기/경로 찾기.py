import sys
input = sys.stdin.readline
graph = []

N = int(input())
for i in range(N):
    graph.append(list(map(int, input().split())))

for i in range(N):
    for j in range(N):
        for k in range(N):
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1
                # print("i=%d j=%d k=%d "%(i,j,k))
for i in graph:
    print(*i)