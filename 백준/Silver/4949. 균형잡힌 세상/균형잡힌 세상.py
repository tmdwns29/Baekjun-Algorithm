while True:
    stack = []
    string = input()
    answer = 'yes'

    if string == '.':
        break
    for i in string:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not len(stack):
                answer = 'no'
                break
            else:
                if stack.pop(-1) != '(':
                    answer = 'no'
        elif i == ']':
            if not len(stack):
                answer = 'no'
                break
            else:
                if stack.pop(-1) != '[':
                    answer = 'no'
        else:
            continue
    if len(stack):
        answer = 'no'
    print(answer)