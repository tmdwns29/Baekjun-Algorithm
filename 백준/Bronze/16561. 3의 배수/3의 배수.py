N = int(input())
num = [0, 0, 0, 1]
cnt = 2

for i in range(4, N//3+1):
    num.append(num[-1]+cnt)
    cnt += 1
print(num[-1])