import sys

N = int(input())
num = [0]*10001 # 정렬할 수 저장할 공간을 인덱스를 이용-> 10000까지

for _ in range(N):
    num[int(sys.stdin.readline())] += 1 # 입력받은 자연수 값을 갖는 num인덱스공간에 1을 더해줌

for i in range(10001):
    if num[i] != 0: # num리스트의 원소값 중 0이 아닌 값이라면,
        for j in range(num[i]): # i를 인덱스로 갖는 공간의 수 만큼 i값(입력한 자연수) 출력(중복값 출력하기 위함)
            print(i)