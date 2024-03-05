from collections import deque

T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    imp = deque(list(map(int, input().split())))
    count = 0
    while imp:
        max_num = max(imp)
        front = imp.popleft()
        M -= 1

        if max_num == front:
            count += 1
            if M < 0:
                print(count)
                break
        else:
            imp.append(front)
            if M<0:
                M = len(imp) - 1