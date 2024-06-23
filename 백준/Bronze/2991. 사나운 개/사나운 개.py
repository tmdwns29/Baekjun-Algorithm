import sys
input = sys.stdin.readline

A,B,C,D = map(int, input().split())
P,M,N = map(int, input().split())
a_dog = A*'1' + B*'0'
b_dog = C*'1' + D*'0'

for i in P,M,N:
    print(int(a_dog[i%len(a_dog)-1]) + int(b_dog[i%len(b_dog)-1]))