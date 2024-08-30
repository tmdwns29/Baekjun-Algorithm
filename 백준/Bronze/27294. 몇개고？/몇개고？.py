import sys
input = sys.stdin.readline

T, S = map(int, input().split())

if not(12<=T<=16) or S:
    print(280)
else:
    print(320)