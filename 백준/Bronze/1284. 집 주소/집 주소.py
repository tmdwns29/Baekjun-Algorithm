import sys
input = sys.stdin.readline

while True:
    N = list(map(str, input().rstrip()))
    if N[-1] == N[0] == '0': break
    length = len(N)+1
    for n in N:
        if n == '1':
            length += 2
        elif n == '0':
            length += 4
        else:
            length += 3
    print(length)