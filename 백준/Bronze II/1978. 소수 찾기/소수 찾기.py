N = int(input())
num = list(map(int, input().split()))
count = 0

for i in num:
    for j in range(2, i+1):
        if i % j == 0:
            if i == j:
                count += 1
            break # i!=j이고 중간에 나눠지는 것을 확인 후에 반복문 탈출
print(count)