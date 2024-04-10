import sys
input = sys.stdin.readline

polynomial = input().rstrip().split('-')
sum_num = []

for i in polynomial:
    sum_ = 0
    tmp = i.split('+')
    for j in tmp:
        sum_ += int(j)
    sum_num.append(sum_)
    
answer = sum_num[0]
for i in range(1, len(sum_num)):
    answer -= sum_num[i]
print(answer)