A, B = map(int, input().split())
A_list = list(str(A))
B_list = list(str(B))
result = 0

for i in A_list:
    for j in B_list:
        result += int(i)*int(j)
print(result)