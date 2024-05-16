import sys
input = sys.stdin.readline

arr = input().rstrip()
stack = []
cnt = 0

for i in range(len(arr)):
    if arr[i] == '(':
        stack.append(i)
    else:
        if arr[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        else:
            stack.pop()
            cnt += 1
print(cnt)