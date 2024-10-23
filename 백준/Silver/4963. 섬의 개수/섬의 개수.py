from collections import deque
import sys
input = sys.stdin.readline

def BFS(a, b):
    q = deque([])
    q.append((a, b))
    maps[a][b] = 0
    
    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx, ny = x+dx, y+dy

            if 0 <= nx < h and 0 <= ny < w and maps[nx][ny]:
                q.append((nx, ny))
                maps[nx][ny] = 0

d = [(-1, 0),(1, 0),(0, 1),(0, -1),
     (1, 1),( -1, 1),(-1, -1), (1, -1)]

while True:
    w,h = map(int, input().split())

    if w == 0 and h == 0: break

    maps = []
    cnt = 0
    for _ in range(h):
        temp = list(map(int, input().split()))
        maps.append(temp)
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                BFS(i, j)
                cnt += 1
    print(cnt)