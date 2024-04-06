import sys
from collections import deque
input = sys.stdin.readline

M, N = map(int,input().split())
tomato = [[] for _ in range(N)]
start = []
res = 0

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(M):
        if temp[j] == 1:
            start.append((i,j))
    tomato[i].extend(temp)

d = [(-1,0),(1,0),(0,-1),(0,1)]

def BFS(start):
    q = deque()
    q.extend(start)
    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx, ny = x+dx, y+dy
            if 0<=nx<N and 0<=ny<M and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                q.append((nx, ny))

BFS(start)

for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    res = max(res, max(i))
print(res-1)