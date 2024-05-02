import sys
input = sys.stdin.readline

N = int(input())
N_num = list(map(int, input().split()))
M = int(input())
M_num = list(map(int, input().split()))

N_num_sort = sorted(N_num)

def BS(start, end, n):
    mid = (start+end)//2

    if start > end: return 0
    if n > N_num_sort[mid]:
        return BS(mid+1, end, n)
    elif n < N_num_sort[mid]:
        return BS(start, mid-1, n)
    else:
        return 1
    
for i in M_num:
    sys.stdout.write("%d "%BS(0, N-1, i))