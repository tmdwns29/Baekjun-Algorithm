import sys
input = sys.stdin.readline

def BFS(n):
    q = []
    q.append(n)
    v[n] = 1

    while q:
        c = q.pop()
        for i in graph[c]:
            if not v[i]:
                q.append(i)
                v[i] = 1


N,M = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

v = [0] * (N+1)
cnt = 0
for i in range(1, N+1):
    if not v[i]:
        BFS(i)
        cnt += 1

print(cnt)