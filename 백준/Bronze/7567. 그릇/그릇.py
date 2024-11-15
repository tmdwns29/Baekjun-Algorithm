import sys
input = sys.stdin.readline

plate = input().rstrip()

height = 10

for i in range(1, len(plate)):
    if plate[i] == plate[i-1]:
        height += 5
    else:
        height += 10
print(height)