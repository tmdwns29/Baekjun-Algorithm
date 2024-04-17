import sys, math
input = sys.stdin.readline

T = int(input())

for i in range(T):
    x, y = map(int, input().split())
    print(math.factorial(y)//(math.factorial(y-x)*math.factorial(x)))