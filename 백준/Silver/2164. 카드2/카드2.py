import sys
from collections import deque
N = int(sys.stdin.readline())
num = deque([i+1 for i in range(N)])

while len(num) > 1:
    num.popleft()
    a = num.popleft()
    num.append(a)

print(num[0])

''' 파이썬은 재귀호출이 1000번으로 제한
    N의 숫자가 최대 500,000번인 것을 고려하면
    카드를 버리고 추가하는 연산이 총 1000번을 초과하므로
    시간복잡도가 상대로 낮은 deque와
    횟수제한이 없는 반복문을 사용'''