import sys

input = sys.stdin.readline

T = int(input())

for i in range(T):
    fassion = dict() # 의상을 저장할 딕셔너리 선언
    n = int(input())
    for _ in range(n):
        a, b = map(str, input().rstrip().split())
        if fassion.get(b) == None: # b종류 의상에 아무것도 없다면,
            fassion[b] = set() # b에 집합자료형 형성
        fassion[b].add(a) # b종류에 a의상 추가

    cnt = 1 # 경우의 수 초기화
    for i in fassion.keys(): # 의상종류(key)를 순회
        # 해당 종류의 각 옷을 입는 경우(옷 개수) + 해당 종류의 옷을 입지 않는 경우(1)
        cnt *= len(fassion[i]) + 1
    print(cnt-1) # 모든 의류를 하나도 입지 않은 경우 제외