import sys
input = sys.stdin.readline

M = int(input())
N = int(input())
num = 1
result = []
while True:
    if num > N: break
    if M <= num*num <= N:
        result.append(num*num)
    num += 1
if not result:
    print(-1)
else:
    print(sum(result))
    print(min(result))