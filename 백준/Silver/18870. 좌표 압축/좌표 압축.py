import sys
input = sys.stdin.readline

N = int(input())
num = list(map(int, input().split()))

''' 입력받은 리스트 원소들의 중복을 없애고, 
    다시 리스트로 지정한 후 정렬'''
arr = sorted(list(set(num)))

dic = {arr[i] : i for i in range(len(arr))} # { 10: 0, -9: 1, 2: 2, 3: 4 }

for i in num:
    sys.stdout.write("%d "% dic[i])