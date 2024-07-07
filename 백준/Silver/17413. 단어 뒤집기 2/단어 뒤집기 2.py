import sys
input = sys.stdin.readline

S = list(map(str, input().rstrip()))
res = ''
tf = False
cnt = 0
stack = []

for i in S:
    if i == '<':
        tf = True
        for _ in range(len(stack)):
            res += stack.pop()

    stack.append(i)

    if i == '>':
        tf = False
        for _ in range(len(stack)):
            res += stack.pop(0)
        
    if i == ' ' and tf == False:
        for s in range(len(stack)):
            if s == 0:
                stack.pop()
                continue
            res += stack.pop()
        res += ' '

if stack:
    for _ in range(len(stack)):
        res += stack.pop()
print(res)