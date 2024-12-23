N = int(input())
voting_result = input().rstrip()

A_cnt = voting_result.count('A')
B_cnt = voting_result.count('B')

if A_cnt > B_cnt:
    print('A')
elif A_cnt < B_cnt:
    print('B')
else:
    print('Tie')