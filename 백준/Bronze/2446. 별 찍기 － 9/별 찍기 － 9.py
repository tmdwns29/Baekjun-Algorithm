import sys
input = sys.stdin.readline

N = int(input())
j = 0
for i in range(2*N-1, 0, -2):
    print(" "*j, end='')
    print("*"*i, end='')
    print()
    j+=1
j -= 1
for i in range(3, 2*N, 2):
    j-=1
    print(" "*j, end='')
    print("*"*i, end='')
    print()