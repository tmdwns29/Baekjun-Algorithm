n = int(input())
member = []
for i in range(n):
    age, name = map(str, input().split())
    age = int(age)
    member.append((age, name)) # age->[0], name->[1]
member.sort(key = lambda x: x[0]) # x에 member가 대입, member[0]번째 요소 기준 정렬
for j in member:
    print(j[0], j[1])