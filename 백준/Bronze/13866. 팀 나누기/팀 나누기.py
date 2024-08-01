a,b,c,d = map(int, input().split())

if a+d > b+c:
    print((a+d)-(b+c))
else:
    print((b+c)-(a+d))