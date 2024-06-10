import sys
input = sys.stdin.readline

t = []
for i in range(3):
    temp = int(input())
    t.append(temp)

if t.count(60) == 3:
    print('Equilateral')
    exit(0)
if sum(t) == 180:
    if t[0]==t[1] or t[1]==t[2] or t[0]==t[2]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')