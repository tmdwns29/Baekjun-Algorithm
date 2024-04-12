from collections import deque
import sys
input = sys.stdin.readline

N,M = map(int, input().split())
miro = [list(map(int, input().rstrip())) for _ in range(N)]

d = [(-1,0),(1,0),(0,-1),(0,1)]

q = deque([(0,0)])

while q:
    x, y = q.popleft() # (1,0) (0,1)
    
    for dx, dy in d: # 1,0
        nx,ny = x+dx, y+dy

        if 0<= nx < N and 0<= ny < M:
            if miro[nx][ny] and miro[x][y]:
                miro[nx][ny] = miro[x][y]+1
                if nx+1==N and ny+1==M:
                    print(miro[-1][-1])
                    exit(0)
                q.append((nx, ny))
    miro[x][y] = 0