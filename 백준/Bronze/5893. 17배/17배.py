N = list(map(int, input().rstrip()))
cnt = 0
int_num = 0

for i in reversed(N):
    int_num += i * (2**cnt)
    cnt += 1

result = bin(int_num*17)[2:]
print(result)