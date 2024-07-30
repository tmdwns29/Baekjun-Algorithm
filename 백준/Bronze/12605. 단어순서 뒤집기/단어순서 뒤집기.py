import sys
input = sys.stdin.readline

N = int(input())

for n in range(N):
    sentence = list(map(str, input().split()))
    print(f'Case #{n+1}: ', end='')
    for i in range(len(sentence)-1, -1, -1):
        print(sentence[i], end=' ')
    print()