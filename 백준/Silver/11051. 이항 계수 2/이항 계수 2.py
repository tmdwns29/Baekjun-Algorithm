import sys, math
input = sys.stdin.readline

N, K = map(int, input().split())

result = math.factorial(N) // (math.factorial(K) * math.factorial(N-K))
print(result%10007)