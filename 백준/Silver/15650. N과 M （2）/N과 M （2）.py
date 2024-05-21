import sys
input = sys.stdin.readline

def DFS(start):
    if len(arr) == M:
        print(*arr)
        return
    
    for i in range(start, N+1):
        if i not in arr:
            arr.append(i)
            DFS(i+1)
            arr.pop()

N,M = map(int, input().split())
arr = []
DFS(1)