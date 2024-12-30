N = int(input())
D, P = 0, 0
for _ in range(N):
    winner = input().rstrip()
    if abs(D-P) == 2:
        continue
    if winner == 'D':
        D += 1
    else:
        P += 1

print(f'{D}:{P}')