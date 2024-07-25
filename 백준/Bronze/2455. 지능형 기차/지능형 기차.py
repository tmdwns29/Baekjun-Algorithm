import sys
input = sys.stdin.readline

person = 0
max_person = 0

for _ in range(4):
    x, y = map(int, input().split())
    person -= x
    person += y
    if max_person < person:
        max_person = person
print(max_person)