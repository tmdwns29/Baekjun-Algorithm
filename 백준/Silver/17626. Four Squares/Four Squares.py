import sys
input = sys.stdin.readline

N = int(input())
arr = [0 if i**0.5%1 else 1 for i in range(N+1)]

min_ = 4
for i in range(int(N**0.5), 0, -1): # (5, 0, -1)
    if arr[N]: # 1 4 9 16 25
        min_ = 1
        break
    elif arr[N-i**2]: # 2 11 18 23 26
        min_ = 2
        break
    else: # 3 5 6 7 8 10 12 13 14 15 17 19 20 21 22 24 27
        for j in range(int((N-i**2)**0.5), 0, -1):
            if arr[(N-i**2)-j**2]:
                min_ = 3
print(min_)