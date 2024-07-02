import sys
input = sys.stdin.readline

ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

x = [ax,bx,cx]
y = [ay,by,cy]

for i in range(3):
    if x.count(x[i]) == 1:
        dx = x[i]
    if y.count(y[i]) == 1:
        dy = y[i]
print(dx,dy)