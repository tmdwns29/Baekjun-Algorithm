import sys
input = sys.stdin.readline

N = int(input())
num = []

for _ in range(N):
    num.append(int(input()))
num.sort()

print(round(sum(num)/N))
print(num[len(num)//2])

dic = dict()
for i in num:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
max_num = max(dic.values())
max_dic = []
for i in dic:
    if max_num == dic[i]:
        max_dic.append(i)
if len(max_dic)>1:
    print(max_dic[1])
else:
    print(max_dic[0])

print(max(num)-min(num))