import sys

N = int(sys.stdin.readline().rstrip())
deque = []

for i in range(N):
    command = sys.stdin.readline().rstrip()
    if 'push_' in command:
        command, value = command.split(' ')
        if 'front' in command:
            deque.insert(0, int(value))
        elif 'back' in command:
            deque.append(int(value))
    elif 'pop_' in command:
        if 'front' in command:
            if len(deque) == 0: print(-1)
            else:
                print(deque[0]) 
                deque.pop(0)
        elif 'back' in command:
            if len(deque) == 0: print(-1)
            else:
                print(deque[-1]) 
                deque.pop(-1)
    elif 'size' in command:
        print(len(deque))
    elif 'empty' in command:
        if len(deque) == 0: print(1)
        else: print(0)
    elif 'front' in command:
        if len(deque) == 0: print(-1)
        else: print(deque[0])
    elif 'back' in command:
        if len(deque) == 0: print(-1)
        else: print(deque[-1])