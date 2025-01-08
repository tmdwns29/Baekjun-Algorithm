import sys
input = sys.stdin.readline

N = int(input())
max_money = -1
for _ in range(N):
    a, b, c = map(int, input().split())
    money = 0

    if a==b==c:
        money = 10000+a*1000
    elif a==b or b==c or a==c:
        if a==b: money = 1000+a*100
        elif b==c: money = 1000+b*100
        elif a==c: money = 1000+c*100
    else:
        money = max(a,b,c)*100
    
    if max_money < money:
        max_money = money
print(max_money)