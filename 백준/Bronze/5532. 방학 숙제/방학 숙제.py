import sys
input = sys.stdin.readline

L = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())

if A / C > B / D:
    if A % C > 0:
        print(L-(A//C+1))
    else:
        print(L-(A//C))
else:
    if B % D > 0:
        print(L-(B//D+1))
    else:
        print(L-(B//D))