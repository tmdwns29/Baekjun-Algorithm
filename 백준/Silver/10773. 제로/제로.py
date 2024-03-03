import sys
input = sys.stdin.readline
N = int(input())
arr=[]

for i in range(N):
    x = int(input())
    if x == 0:
        arr.pop()
    else:
        arr.append(x)
print(sum(arr))