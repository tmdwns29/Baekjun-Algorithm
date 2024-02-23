import sys

N = int(sys.stdin.readline().rstrip())
stack = []

for i in range(N):
    command = sys.stdin.readline().rstrip()
    if 'push' in command:
        command, value = command.split(' ')
        stack.append(int(value))
    elif 'pop' in command:
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop(-1)
    elif 'size' in command:
        print(len(stack))
    elif 'empty' in command:
        if len(stack) == 0: print(1)
        else: print(0)
    elif 'top' in command:
        if len(stack) == 0: print(-1)
        else: print(stack[-1])