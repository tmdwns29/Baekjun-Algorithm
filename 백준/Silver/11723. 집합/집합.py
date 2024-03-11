import sys
input = sys.stdin.readline
S = []
M = int(input())
for i in range(M):
    calc = input().rstrip()
    if calc == 'all' or calc == 'empty':
        if calc == 'all':
            S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11,12,13,14,15,16,17,18,19,20]
        elif calc == 'empty':
            S = []
    else:
        cal, x = calc.split(' ')
        x = int(x)
        if x not in S and cal == 'add':
            S.append(x)
        elif x in S and cal == 'remove':
            S.pop(S.index(x))
        elif cal == 'check':
            if x in S: print(1)
            else: print(0)
        elif cal == 'toggle':
            if x in S:
                S.pop(S.index(x))
            else:
                S.append(x)