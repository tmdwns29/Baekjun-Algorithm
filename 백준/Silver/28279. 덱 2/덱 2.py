from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
deq = deque([])

for i in range(N):
    command = input().rstrip()
    if len(command) > 1:
        X = int(command.split()[1])
        if '1' == command[0]:
            deq.appendleft(X)
        else:
            deq.append(X)
    elif '3' == command[0]:
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif '4' == command[0]:
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif '5' == command[0]:
        print(len(deq))
    elif '6' == command[0]:
        print(1 if not deq else 0)
    elif '7' == command[0]:
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif '8' == command[0]:
        if deq:
            print(deq[-1])
        else:
            print(-1)