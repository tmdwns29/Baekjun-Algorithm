import sys
input = sys.stdin.readline

M = int(input())
N = int(input())
num_list = []

for n in range(M, N+1):
    flag = True
    for i in range(2, n):
        if n % i == 0:
            flag = False
            break
    if flag:
        num_list.append(n)

if M == 1:
    num_list.pop(0)

if not num_list:
    print(-1)
else:
    print(sum(num_list))
    print(min(num_list))