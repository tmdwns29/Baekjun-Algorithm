import sys
input = sys.stdin.readline

N = int(input())
P = list(map(int, input().split()))

num,j = [], 1 # 순서변수와 소요시간을 저장할 리스트 선언
for i in P:
    num.append((j,i)) # num에 소요시간들을 순서와 함께 복사
    j+=1
num.sort(key=lambda x: x[1]) # 소요시간의 오름차순으로 정렬
Pi,res = 0,0 # 각 소요시간을 저장할 변수와 최솟값을 저장할 변수 선언

for i in num:
    Pi += i[1] # 각 Pi기준으로 소요시간을 저장하고,  
    res += Pi # 그 Pi를 모두 더한 값(최솟값)
sys.stdout.write("%d"%res)
