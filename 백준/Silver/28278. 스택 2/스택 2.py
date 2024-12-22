import sys
input = sys.stdin.readline

N = int(input())
stack = []

for i in range(N):
    command = input().rstrip()
    if ' ' in command:
        num = int(command.split()[1])
        stack.append(num)
        continue

    command = int(command)

    if command == 2:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif command == 3:
        print(len(stack))
    elif command == 4:
        if stack:
            print(0)
        else:
            print(1)
    elif command == 5:
        if stack:
            print(stack[-1])
        else:
            print(-1)