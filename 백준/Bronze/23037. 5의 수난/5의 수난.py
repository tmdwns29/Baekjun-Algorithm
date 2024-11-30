N = list(map(int, input().rstrip()))
res = 0
for n in N:
    res += n**5
print(res)