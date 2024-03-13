import sys
input = sys.stdin.readline

zero = [1,0,1] # 숫자가 0일 때 0이 1
one  = [0,1,1] # 숫자가 1일 때 1이 1
               # 숫자가 2일 때 0, 1이 각각 1,1

def fibonacci(n):
    length = len(zero)
    if n >= length: # 기본 3 이상이면,
        for i in range(length, n+1):
            zero.append(zero[i-1]+zero[i-2])
            one.append(one[i-1]+one[i-2])
    print('%d %d'%(zero[n], one[n]))

T = int(input())

for _ in range(T):
    fibonacci(int(input()))