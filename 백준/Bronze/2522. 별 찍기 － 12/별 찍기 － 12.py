N = int(input())

for i in range(1, N+1):
    print(' '*(N-i)+'*'*i)
for j in range(1, N):
    print(' '*j+'*'*(N-j))