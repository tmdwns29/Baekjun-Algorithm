from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()

for _ in range(N):
    command = input().rstrip()
    if 'push' in command:
        com, num = command.split()
        queue.append(num)
    elif 'pop' in command:
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif 'size' in command:
        print(len(queue))
    elif 'empty' in command:
        if not queue:
            print(1)
        else:
            print(0)
    elif 'front' in command:
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif 'back' in command:
        if not queue:
            print(-1)
        else:
            print(queue[-1])