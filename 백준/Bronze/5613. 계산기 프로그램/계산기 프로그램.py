expression = []

while '=' not in expression:
    temp = input().rstrip()
    expression.append(temp)

result = int(expression[0])

for i in range(2, len(expression), 2):
    if expression[i-1] == '+':
        result += int(expression[i])
    elif expression[i-1] == '-':
        result -= int(expression[i])
    elif expression[i-1] == '*':
        result *= int(expression[i])
    elif expression[i-1] == '/':
        result //= int(expression[i])

print(result)