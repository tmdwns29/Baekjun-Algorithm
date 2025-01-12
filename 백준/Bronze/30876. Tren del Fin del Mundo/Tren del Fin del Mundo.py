N = int(input())
rail = []

for _ in range(N):
    xi, yi = map(int, input().split())
    rail.append((xi, yi))

rail.sort(key=lambda x:x[1])

print(*rail[0])