from collections import deque
import sys
input = sys.stdin.readline

N,R,C = map(int, input().split())
bat = [['.']*N for _ in range(N)]
d = [(-1,-1), (1, 1), (-1, 1), (1, -1)]

def BFS(a,b):
    q = deque([(a,b)])
    
    while q:
        x,y = q.popleft()

        for dx,dy in d:
            nx,ny = x+dx, y+dy

            if 0<=nx<N and 0<=ny<N and bat[nx][ny] == '.':
                bat[nx][ny] = 'v'
                q.append((nx, ny))
BFS(R,C)

for i in bat:
    print(''.join(i))