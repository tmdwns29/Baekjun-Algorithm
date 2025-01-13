C, K, P = map(int, input().split())
answer = 0

for n in range(C+1):
    answer += K*n+P*n**2
print(answer)