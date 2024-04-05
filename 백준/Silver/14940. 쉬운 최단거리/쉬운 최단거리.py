import sys
from collections import deque
input = sys.stdin.readline

d = [(1,0), (0,1), (-1,0), (0,-1)]

def BFS(start):
    q = deque([start])
    visit[start[0]][start[1]] = 0

    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx, ny = x+dx, y+dy

            if 0<=nx<n and 0<=ny<m and visit[nx][ny] == -1: # 범위를 벗어나지 않는,
                if ground[nx][ny] == 0: # 갈 수없는 땅이면
                    visit[nx][ny] = 0 # 0으로 처리
                elif ground[nx][ny] == 1: # 갈 수있는 땅이면,
                    
                    # 이전 값에 1을 더하여 이동 거리값 저장
                    visit[nx][ny] = visit[x][y] + 1
                    q.append((nx, ny)) # 다음 탐색 위치 추가        

n, m = map(int, input().split())
ground = [[] for _ in range(n)]
visit = [[-1] * m for _ in range(n)]

for i in range(n):
    temp = list(map(int, input().split()))
    for j in range(m):
        if temp[j] == 2:
            start = (i, j)
            break
    ground[i].extend(temp)

BFS(start)

for i in range(n):
    for j in range(m):
        if ground[i][j] == 0:
            print(0, end=' ')
        else:
            print(visit[i][j], end=' ')
    print()