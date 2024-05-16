arr = []
x,y = 0,0
max_num = 0

for i in range(9):
  temp = list(map(int, input().split()))
  if max_num <= max(temp):
    max_num = max(temp)
    x,y = i+1, temp.index(max(temp))+1
  arr.append(temp)
print(arr[x-1][y-1])
print(x, y)