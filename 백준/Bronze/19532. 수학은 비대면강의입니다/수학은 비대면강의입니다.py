import sys
input = sys.stdin.readline

a,b,c,d,e,f = map(int, input().split())
X, Y = 0, 0
for x in range(-999, 1000):
    for y in range(-999, 1000):
        if a*x + b*y == c and d*x + e*y ==f:
            X,Y = x,y
            break
print(X, Y)