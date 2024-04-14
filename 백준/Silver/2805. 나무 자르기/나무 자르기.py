import sys
input = sys.stdin.readline

N, M = map(int, input().split())
height = list(map(int, input().split()))
start,end = 1, max(height)

while start <= end:
    cut = (start + end)//2
    sum = 0
    
    for i in height:
        if i >= cut:
            sum += i-cut
    if sum >= M:
        start = cut+1
    else:
        end = cut-1

sys.stdout.write("%d\n"%end)