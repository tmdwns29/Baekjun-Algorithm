# [Silver III] 통계학 - 2108 

[문제 링크](https://www.acmicpc.net/problem/2108) 

### 성능 요약

메모리: 52504 KB, 시간: 488 ms

### 분류

구현, 수학, 정렬

### 제출 일자

2024년 3월 7일 12:15:02

### 문제 설명

<p>수를 처리하는 것은 통계학에서 상당히 중요한 일이다. 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.</p>

<ol>
	<li>산술평균 : N개의 수들의 합을 N으로 나눈 값</li>
	<li>중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값</li>
	<li>최빈값 : N개의 수들 중 가장 많이 나타나는 값</li>
	<li>범위 : N개의 수들 중 최댓값과 최솟값의 차이</li>
</ol>

<p>N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다. 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.</p>

### 출력 

 <p>첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.</p>

<p>둘째 줄에는 중앙값을 출력한다.</p>

<p>셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.</p>

<p>넷째 줄에는 범위를 출력한다.</p>

### 풀이
 <p>중앙값, 범위는 어렵지 않게 구할 수 있었다. 산술평균은 반올림 구현하는 함수를 잊고있어서 다시 찾아보고 풀었다. 문제는 최빈값이었는데 처음에는 count메서드를 이용해서 그 값이 1이 넘는 경우에만 다른 리스트에 count된 값을 추가하는 방식으로 시도했다. 하지만 시간이 초과되었고, 다른 분들의 풀이를 참고했다. </p>

 ~~~python
import sys
input = sys.stdin.readline

N = int(input())
num = []

for _ in range(N):
    num.append(int(input()))
num.sort()

print(round(sum(num)/N))
print(num[len(num)//2])

dic = dict() # 딕셔너리 선언
for i in num: # num숫자들을 하나씩 순회하며
    if i in dic: # dic에 num숫자들이 있으면
        dic[i] += 1 # 원래 값에 +1
    else: # dic에 num 숫자들이 없으면
        dic[i] = 1 # 1추가
max_num = max(dic.values()) # 중복값이 가장 많은 수 저장
max_dic = [] # 중복값의 최대값을 저장하는 리스트 선언
for i in dic: # dic의 중복값들을 하나씩 순회하며
    if max_num == dic[i]: # 그 값이 최대값과 같다면
        max_dic.append(i) # 그 값을 추가
if len(max_dic)>1: # 최빈값이 2개 이상이면
    print(max_dic[1]) # 두번째로 작은 값 출력
else: # 최빈값이 1개이면
    print(max_dic[0]) # 그 값을 출력

print(max(num)-min(num))
 ~~~
