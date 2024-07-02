import sys
input = sys.stdin.readline

ax, ay = map(int, input().split())
bx, by = map(int, input().split())
cx, cy = map(int, input().split())

x = [ax,bx,cx]
y = [ay,by,cy]
x.sort()
y.sort()

if x[0]==x[1]: print(x[2], end=' ')
else: print(x[0], end=' ')

if y[0]==y[1]: print(y[2], end='')
else: print(y[0], end='')