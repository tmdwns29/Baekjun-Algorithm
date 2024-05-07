from collections import deque
import sys, copy
input = sys.stdin.readline

def BFS():
    q = deque()
    tmp_arr = copy.deepcopy(arr)

    for i in range(N):
        for j in range(M):
            if tmp_arr[i][j] == 2:
                q.append((i,j))
    while q:
        x, y = q.popleft()

        for dx, dy in d:
            nx,ny = x+dx, y+dy

            if 0<=nx<N and 0<=ny<M and tmp_arr[nx][ny] == 0:
                tmp_arr[nx][ny] = 2
                q.append((nx, ny))
    
    global result
    cnt = 0

    for i in range(N):
        for j in range(M):
            if tmp_arr[i][j] == 0:
                cnt += 1
    result = max(result, cnt)

def wall(cnt):
    if cnt == 3:
        BFS()
        return
                    
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(cnt+1)
                arr[i][j] = 0

N,M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
d = [(-1,0),(1,0),(0,-1),(0,1)]
result = 0

wall(0)
print(result)