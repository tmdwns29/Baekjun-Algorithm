num = list(map(int, input().split()))
result = []

for i in num:
    num_arr = []
    for j in range(1, i+1):
        if i % j == 0:
            num_arr.append(j)
    result.append(num_arr)
max_num=0
for a in result[0]:
    for b in result[1]:
        if a == b:
            max_num = a
print(max_num)
print(num[0]//max_num*num[1])