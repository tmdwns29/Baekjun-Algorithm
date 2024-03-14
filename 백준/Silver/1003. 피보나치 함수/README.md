# [Silver III] 피보나치 함수 - 1003 

[문제 링크](https://www.acmicpc.net/problem/1003) 

### 성능 요약

메모리: 31120 KB, 시간: 40 ms

### 분류

다이나믹 프로그래밍

### 제출 일자

2024년 3월 13일 19:07:12

### 문제 설명

<p>다음 소스는 N번째 피보나치 수를 구하는 C++ 함수이다.</p>

<pre>int fibonacci(int n) {
    if (n == 0) {
        printf("0");
        return 0;
    } else if (n == 1) {
        printf("1");
        return 1;
    } else {
        return fibonacci(n‐1) + fibonacci(n‐2);
    }
}
</pre>

<p><code>fibonacci(3)</code>을 호출하면 다음과 같은 일이 일어난다.</p>

<ul>
	<li><code>fibonacci(3)</code>은 <code>fibonacci(2)</code>와 <code>fibonacci(1)</code> (첫 번째 호출)을 호출한다.</li>
	<li><code>fibonacci(2)</code>는 <code>fibonacci(1)</code> (두 번째 호출)과 <code>fibonacci(0)</code>을 호출한다.</li>
	<li>두 번째 호출한 <code>fibonacci(1)</code>은 1을 출력하고 1을 리턴한다.</li>
	<li><code>fibonacci(0)</code>은 0을 출력하고, 0을 리턴한다.</li>
	<li><code>fibonacci(2)</code>는 <code>fibonacci(1)</code>과 <code>fibonacci(0)</code>의 결과를 얻고, 1을 리턴한다.</li>
	<li>첫 번째 호출한 <code>fibonacci(1)</code>은 1을 출력하고, 1을 리턴한다.</li>
	<li><code>fibonacci(3)</code>은 <code>fibonacci(2)</code>와 <code>fibonacci(1)</code>의 결과를 얻고, 2를 리턴한다.</li>
</ul>

<p>1은 2번 출력되고, 0은 1번 출력된다. N이 주어졌을 때, <code>fibonacci(N)</code>을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 테스트 케이스의 개수 T가 주어진다.</p>

<p>각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어진다. N은 40보다 작거나 같은 자연수 또는 0이다.</p>

### 출력 

 <p>각 테스트 케이스마다 0이 출력되는 횟수와 1이 출력되는 횟수를 공백으로 구분해서 출력한다.</p>

### 풀이
 ~~~python
import sys
input = sys.stdin.readline

zero = [1,0,1]
one  = [0,1,1]

def fibonacci(num):
    length = len(zero)
    if length <= num:
        for i in range(length, num+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print("%d %d"%(zero[num], one[num]))
T = int(input())
for i in range(T):
    fibonacci(int(input()))
 ~~~
 <p>피보나치 값을 구하는 것이 아닌 0과 1의 출력되는 횟수를 구하면 된다. 0의 피보나치 수는 0, 1의 피보나치 수는 1, 따라서 2의 피보나치 수는 0과 1이 각각 하나씩 출력된다. 0과1을 저장할 리스트를 선언하여 0,1,2일 때의 호출된 0과1의 수를 각각 초기화해준다. <code>zero=[1,0,1], one=[0,1,1]</code></p>
 <p>함수에서 0또는 1의 출력 횟수를 저장할 리스트의 길이를 length로 초기화하고, if문에서 입력받은 수가 length보다 같거나 큰 경우에 그 차이만큼 for문을 통해서 각 이전 2개의 수를 더한 값(0과 1의 출력 횟수)을 저장한다. 저장이 끝나면 num번째 인덱스에 접근하여 최종적으로 0과 1의 출력횟수를 출력한다. </p>
