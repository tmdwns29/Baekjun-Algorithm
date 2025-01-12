import math
N = int(input())

rings = list(map(int, input().split()))

for i in range(1, N):
    gcd_num = math.gcd(rings[0], rings[i])
    print(f'{rings[0] // gcd_num}/{rings[i] // gcd_num}')