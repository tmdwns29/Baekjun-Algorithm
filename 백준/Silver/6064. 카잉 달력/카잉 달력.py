import sys
input = sys.stdin.readline

def calc(m,n,x,y):
    while x <= m*n:
        if (x-y) % n == 0:
            return x
        x += m
    return -1

T = int(input())
cnt = 0

for _ in range(T):
    M,N,x,y = map(int, input().split())
    print(calc(M,N,x,y))