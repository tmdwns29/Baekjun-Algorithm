import sys
input = sys.stdin.readline
total = int(input())
prices = 0
for _ in range(9):
    prices += int(input())
print(total-prices)