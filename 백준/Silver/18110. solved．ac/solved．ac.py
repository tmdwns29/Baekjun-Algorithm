import sys
N = int(input())

def banolim(num): # 사사오입 함수
    return int(num) + (1 if num - int(num) >= 0.5 else 0)

if not N: print(0) # 의견이 없으면 0을 출력
else:
    num = [int(sys.stdin.readline()) for _ in range(N)]
    A = banolim(N * 0.15)
    num.sort()
    print(banolim(sum(num[A:-A] if A else num)/(N-(A*2))))
    ''' A가 0이 아니라면 num[A:-A]의 합
    A가 0이라면 num전체 합
    A가 0이면 나누는 수도 num전체 길이로 나눔(N)
    파이썬의 round함수는 오사오입(5미만 숫자는 내리고, 5이상 숫자는 올림)
    ㄴ만약 반올림할 자릿수가 5일 경우 5의 앞자리가 홀수인 경우 올림, 짝수인 경우 내림)
    직접 사사오입 함수를 구현해야함
    부동소수점 이해 필수'''
