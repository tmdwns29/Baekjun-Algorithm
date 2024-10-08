import sys
input = sys.stdin.readline

A, B = map(int, input().split())
C, D = map(int, input().split())

if A + D < C + B:
    print(A + D)
else:
    print(C + B)