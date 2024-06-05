import sys
input = sys.stdin.readline  

N = int(input())
answer = 0
for i in range(N):
    word = input().rstrip()
    result = False
    for i in range(len(word)):
        cnt = 0
        for j in range(i+1, len(word)):
            if word[i] != word[j]:
                cnt += 1
            else:
                if cnt == 0:
                    continue
                else:
                    result = True
    if not result:
        answer+=1 

print(answer)