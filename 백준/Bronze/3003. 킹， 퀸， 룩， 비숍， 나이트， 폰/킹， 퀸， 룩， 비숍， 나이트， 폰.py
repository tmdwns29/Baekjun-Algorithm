import sys
input = sys.stdin.readline

pieces = list(map(int, input().split()))
chess = [1,1,2,2,2,8]

for i in range(6):
    if chess[i] > pieces[i]:
        sys.stdout.write("%d "%(chess[i] - pieces[i]))
    elif chess[i] < pieces[i]:
        sys.stdout.write("%d "%-(pieces[i]-chess[i]))
    else:
        sys.stdout.write("%d "%0)