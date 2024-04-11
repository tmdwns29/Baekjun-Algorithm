import sys
input = sys.stdin.readline

def BFS(n):
    q = []
    q.append(n)
    visit = [0 for _ in range(N+1)]
    visit[n] = 1
    
    while q:
        c = q.pop(0)
        
        for i in relation[c]:
            if not visit[i]:
                q.append(i)
                visit[i] = visit[c] + 1

    return sum(visit)

N, M = map(int, input().split())
relation = [[] for _ in range(N+1)]
res=[]

for i in range(M):
    A, B = map(int, input().split())
    if A not in relation[B] and B not in relation[A]:
        relation[A].append(B)
        relation[B].append(A)

for i in range(1, N+1):
    res.append((i, BFS(i)))

res.sort(key=lambda x : x[0])
res.sort(key=lambda y : y[1])

print(res[0][0])