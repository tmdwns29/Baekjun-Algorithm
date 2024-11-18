passengers = 0
max_num = 0

for i in range(10):
    a, b = map(int, input().split())
    passengers -= a
    passengers += b

    if max_num < passengers:
        max_num = passengers
print(max_num)