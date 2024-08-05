import sys
input = sys.stdin.readline

N = int(input())
book_list = dict()

for _ in range(N):
    temp = input().rstrip()
    if temp not in book_list:
        book_list[temp] = 1
    else:
        book_list[temp] += 1

max_value = max(book_list.values())

best = []
for key, value in book_list.items():
    if value == max_value:
        best.append(key)

best = sorted(best)
print(best[0])