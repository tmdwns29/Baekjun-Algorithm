import sys
input = sys.stdin.readline

T = int(input())

for t in range(T):
    N = int(input())
    binary_num = ''
    res = []
    while N != 0:
        binary_num += str(N % 2)
        N //= 2
    for i in range(len(binary_num)):
        if binary_num[i] == '1':
            res.append(i)
    print(*res)