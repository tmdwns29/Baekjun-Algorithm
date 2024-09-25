import sys
input = sys.stdin.readline

Month = int(input())
Day = int(input())

if Month > 2:
    print('After')
elif Month < 2:
    print('Before')
else:
    if Day > 18:
        print('After')
    elif Day < 18:
        print('Before')
    else:
        print('Special')