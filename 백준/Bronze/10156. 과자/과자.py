import sys
input = sys.stdin.readline

K,N,M = map(int, input().split())
if K*N-M < 0:
    print(0)
else:
    print(K*N-M)