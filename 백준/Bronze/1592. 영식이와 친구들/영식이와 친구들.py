import sys
input = sys.stdin.readline  

N,M,L = map(int, input().split())
arr = [0]*N

i = 0
arr[i] = 1

while True:
    if arr[i] == M:
        print(sum(arr)-1)
        break
    if not(arr[i] % 2):
        i = abs((i-L) % N)
        arr[i] += 1
    else:
        i = (i+L)%N
        arr[i] += 1