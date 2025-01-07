import sys
input = sys.stdin.readline

yeondo = input().rstrip()
N = int(input())

max_rate = -1
result = ''
team_name = []

for i in range(N):
    team_name.append(input().rstrip())
team_name.sort()

for i in range(N):
    sum_name = team_name[i] + yeondo

    L = sum_name.count('L')
    O = sum_name.count('O')
    V = sum_name.count('V')
    E = sum_name.count('E')

    win_rate = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100

    if max_rate < win_rate:
        max_rate = win_rate
        result = team_name[i]
print(result)