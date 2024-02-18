import sys
N = int(input())

def banolim(num):
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

if not N: print(0)
else:
    num = [int(sys.stdin.readline()) for _ in range(N)]
    A = banolim(N * 0.15)
    num.sort()
    print(banolim(sum(num[A:-A] if A else num)/(N-(A*2))))
    ''' A가 0이 아니라면 num[A:-A]의 합
    A가 0이라면 num전체 합
    A가 0이면 나누는 수도 num전체 길이로 나눔(N)
    부동소수점?'''