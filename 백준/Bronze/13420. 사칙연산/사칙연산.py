T = int(input())

for i in range(T):
    exp = list(map(str, input().rstrip().split()))
    result = 'correct'

    match exp[1]:
        case '+':
            if int(exp[0]) + int(exp[2]) != int(exp[4]):
                result = 'wrong answer'
        case '-':
            if int(exp[0]) - int(exp[2]) != int(exp[4]):
                result = 'wrong answer'
        case '*':
            if int(exp[0]) * int(exp[2]) != int(exp[4]):
                result = 'wrong answer'
        case '/':
            if int(exp[0]) / int(exp[2]) != int(exp[4]):
                result = 'wrong answer'
    print(result)