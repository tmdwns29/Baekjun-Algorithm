import sys
input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
students = []
person = 1

for n in numbers:
    if n == 0:
        students.append(person)
    else:
        students.insert(-n, person)
    person += 1
print(*students)