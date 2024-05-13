from collections import deque
import sys
input = sys.stdin.readline

def BFS(a, b, h):
    q = deque([(a,b)])

    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx,ny = x+dx, y+dy

            if 0<=nx<N and 0<=ny<N and not visit[nx][ny]:
                if h < arr[nx][ny]:
                    visit[nx][ny] = 1
                    q.append((nx,ny))

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
d = [(-1,0),(1,0),(0,-1),(0,1)]

area = 1
for k in range(max(map(max, arr))):
    visit = [[0]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > k and not visit[i][j]:
                cnt += 1
                visit[i][j] = 1
                BFS(i,j,k)
    area = max(area, cnt)
print(area)