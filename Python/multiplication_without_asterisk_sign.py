# TODO: what if one or both numbers are negative

def multiply(num1, num2):
    result = 0
    for _ in range(num1):
        result += num2
    print(f'{num1} * {num2} = {result}')

num1 = 4
num2 = 5
multiply(num1, num2)
