import sys
from collections import deque
input = sys.stdin.readline

N, K = map(int, input().split())
visit = [0]*100001

def BFS(n):
    q = deque()
    q.append(n)

    visit[n] = 0 # 시작점은 아직 이동하지 않은 상태

    while q:
        c = q.popleft()
        if c == K:
            return visit[K]
        for i in (c+1, c-1, c*2):
            if 0<= i <100001 and not visit[i]:
                visit[i] = visit[c] + 1
                q.append(i)

print(BFS(N))