# [Silver V] 집합 - 11723 

[문제 링크](https://www.acmicpc.net/problem/11723) 

### 성능 요약

메모리: 130832 KB, 시간: 1160 ms

### 분류

비트마스킹, 구현

### 제출 일자

2024년 3월 11일 12:52:37

### 문제 설명

<p>비어있는 공집합 S가 주어졌을 때, 아래 연산을 수행하는 프로그램을 작성하시오.</p>

<ul>
	<li><code>add x</code>: S에 x를 추가한다. (1 ≤ x ≤ 20) S에 x가 이미 있는 경우에는 연산을 무시한다.</li>
	<li><code>remove x</code>: S에서 x를 제거한다. (1 ≤ x ≤ 20) S에 x가 없는 경우에는 연산을 무시한다.</li>
	<li><code>check x</code>: S에 x가 있으면 1을, 없으면 0을 출력한다. (1 ≤ x ≤ 20)</li>
	<li><code>toggle x</code>: S에 x가 있으면 x를 제거하고, 없으면 x를 추가한다. (1 ≤ x ≤ 20)</li>
	<li><code>all</code>: S를 {1, 2, ..., 20} 으로 바꾼다.</li>
	<li><code>empty</code>: S를 공집합으로 바꾼다.</li>
</ul>

### 입력 

 <p>첫째 줄에 수행해야 하는 연산의 수 M (1 ≤ M ≤ 3,000,000)이 주어진다.</p>

<p>둘째 줄부터 M개의 줄에 수행해야 하는 연산이 한 줄에 하나씩 주어진다.</p>

### 출력 

 <p><code>check</code> 연산이 주어질때마다, 결과를 출력한다.</p>

### 풀이
 <p>로직 자체는 크게 어렵지 않은 난이도라고 생각한다. 실행시간이 관건인데 처음에 생각했던 코드로 작성했을 때 초과될 줄 알았지만 예상 외로 정답처리가 됐다. 실행시간을 줄이고자 all항목에서 for문을 쓰지않고 리스트 초기화에서 숫자를 일일이 써줬는데 다시 생각해보니 수가 크지 않아서 별 의미가 없었던 거 같다. 다른 분들의 풀이에서는 집합이라는 키워드에 걸맞게 set()함수를 이용한게 많이 보였다. set()함수의 요소들은 순서가 없기 때문에 인덱스로 접근할 수 없다. 문제에서도 순서를 요구하는 부분은 없고 단순히 추가, 삭제, 존재여부만 보기 때문에 set()의 쓰임은 적절하다고 생각한다.</p>

 ~~~python
 import sys
input = sys.stdin.readline
S = []
M = int(input())
for i in range(M):
    calc = input().rstrip()
    if calc == 'all' or calc == 'empty':
        if calc == 'all':
            S = [j for i in range(1,21)]
        elif calc == 'empty':
            S = []
    else:
        cal, x = calc.split(' ')
        x = int(x)
        if x not in S and cal == 'add':
            S.append(x)
        elif x in S and cal == 'remove':
            S.pop(S.index(x))
        elif cal == 'check':
            if x in S: print(1)
            else: print(0)
        elif cal == 'toggle':
            if x in S:
                S.pop(S.index(x))
            else:
                S.append(x)
 ~~~

#### 다른 분들의 풀이
~~~python
import sys

m = int(sys.stdin.readline())
S = set()

for _ in range(m):
    temp = sys.stdin.readline().strip().split()
    
    if len(temp) == 1:
        if temp[0] == "all":
            S = set([i for i in range(1, 21)])
        else:
            S = set()
    
    else:
        func, x = temp[0], temp[1]
        x = int(x)

        if func == "add":
            S.add(x)
        elif func == "remove":
            S.discard(x)
        elif func == "check":
            print(1 if x in S else 0)
        elif func == "toggle":
            if x in S:
                S.discard(x)
            else:
                S.add(x)
~~~
