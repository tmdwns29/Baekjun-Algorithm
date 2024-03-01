import sys
input = sys.stdin.readline

N = int(input())
cnt = 0 # 카운트 변수 선언
result = 666 # 

while True:
    if '666' in str(result): # 666이 result에 존재할 때
        cnt += 1 # 1증가
    if cnt == N: # 위에서 증가된 cnt값이 N과 같으면(N번째로 작은 종말의 수)
        break # 반복문 종료
    result += 1 # 666을 성립하기 위해 result변수에 1씩 증가
print(result)