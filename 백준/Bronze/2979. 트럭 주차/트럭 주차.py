import sys
input = sys.stdin.readline

A, B, C = map(int, input().split())
time_table = [0] * 101
price = 0

for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        time_table[i] += 1

for cars in time_table:
    if cars == 1:
        price += A
    elif cars == 2:
        price += B*2
    elif cars == 3:
        price += C*3
print(price)