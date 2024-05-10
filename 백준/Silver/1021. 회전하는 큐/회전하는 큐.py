from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
queue = deque([i for i in range(1, N+1)])
arr = deque(list(map(int, input().split())))
cnt = 0

while arr:
    if arr[0] == queue[0]:
        queue.popleft()
        arr.popleft()
        continue
    if abs(queue.index(arr[0])-0) < abs(queue.index(arr[0])-len(queue)):
        l = queue.popleft()
        queue.append(l)
        cnt+=1
    else:
        r = queue.pop()
        queue.appendleft(r)
        cnt+=1

print(cnt)