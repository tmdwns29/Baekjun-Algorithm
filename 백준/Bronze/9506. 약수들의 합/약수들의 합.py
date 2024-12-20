import sys
input = sys.stdin.readline

while True:
    N = int(input())
    if N == -1: break
    num_list = [1]
    for i in range(2, N):
        if N % i == 0:
            num_list.append(i)
    if N == sum(num_list):
        print(f'{N} = ', end='')
        print(*num_list, sep=' + ')
    else:
        print(f'{N} is NOT perfect.')