import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
A.sort(reverse=True)
B = list(map(int, input().split()))
B.sort()
sum = 0

for i in range(N):
    sum += A[i]*B[i]
print(sum)