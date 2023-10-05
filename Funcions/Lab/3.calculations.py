input_operator = input()
first_num = int(input())
second_num = int(input())


def solve(operator,number1, number2):
    if input_operator == "multiply":
        return number1 * number2
    elif input_operator == "divide":
        return number1 // number2
    elif input_operator == "add":
        return number1 + number2
    elif input_operator == "subtract":
        return number1 - number2


print(solve(input_operator, first_num, second_num))
