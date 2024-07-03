import sys
input = sys.stdin.readline

N = int(input())
res = 1
week = 604800

for n in range(1, N+1):
    res *= n
print(res // week)