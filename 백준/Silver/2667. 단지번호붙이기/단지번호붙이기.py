import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
Map = [[]for _ in range(N)]
d = [(-1,0), (1,0), (0,-1), (0,1)]

for i in range(N):
    temp = list(input().rstrip())
    for j in temp:
        Map[i].append(int(j))

def BFS(a,b):
    q = deque([(a,b)])
    cnt = 0
    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx, ny = x+dx, y+dy

            if 0<=nx<N and 0<=ny<N:
                if Map[nx][ny]:
                    q.append((nx,ny))
                    cnt += 1
                Map[nx][ny] = 0
    if not cnt: return 1
    else: return cnt

res = []
for i in range(N):
    for j in range(N):
        if Map[i][j]:
            res.append(BFS(i,j))
res = sorted(res)
L = len(res)
print(L)
for k in range(L):
    print(res[k])