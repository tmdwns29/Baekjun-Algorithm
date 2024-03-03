N = int(input())
arr=[]
for i in range(N):
    x = int(input())
    if x == 0:
        arr.pop(-1)
    else:
        arr.append(x)
print(sum(arr))