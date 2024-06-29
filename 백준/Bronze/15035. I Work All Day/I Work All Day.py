import sys
input = sys.stdin.readline

N = int(input())
H = list(map(int, input().split()))
T = int(input())
setting = []
for i in H:
    setting.append((i,T%i))
setting.sort(key=lambda x: x[1])
print(setting[0][0])