N = int(input())
cnt = 0

for _ in range(N):
    word = input()
    cnt += len(word)
print(cnt)