
input_numbers = input()

numbers = input_numbers.split()

rounded_numbers = [round(float(number)) for number in numbers]

print(rounded_numbers)