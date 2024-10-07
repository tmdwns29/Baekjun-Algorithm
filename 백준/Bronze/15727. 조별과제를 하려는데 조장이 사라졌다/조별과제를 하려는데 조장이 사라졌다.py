import sys
input = sys.stdin.readline

L = int(input())

if L % 5 == 0:
    print(L // 5)
else:
    print(L // 5 + 1)