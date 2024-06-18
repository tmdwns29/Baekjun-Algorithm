from collections import deque
import sys
input = sys.stdin.readline

def BFS(a,b):
    q = deque([(a,b)])
    area = 0

    while q:
        x, y = q.popleft()
        for dx, dy in d:
            nx,ny = x+dx, y+dy

            if 0<=nx<N and 0<=ny<M and not paper[nx][ny]:
                q.append((nx,ny))
                paper[nx][ny] = 1
                area += 1
    if area == 0: return area+1
    else: return area

M,N,K = map(int, input().split())
paper = [[0]*M for _ in range(N)]
d = [(-1,0),(1,0),(0,-1),(0,1)]
area_list = []
cnt = 0

for i in range(K):
    lx,ly, rx,ry = map(int, input().split())
    for x in range(lx, rx):
        for y in range(ly, ry):
            paper[x][y] = 1

for x in range(N):
    for y in range(M):
        if not paper[x][y]:
            area_list.append(BFS(x,y))
            cnt += 1
area_list.sort()

print(cnt)
print(*area_list)