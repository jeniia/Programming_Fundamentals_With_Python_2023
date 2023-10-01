def find_capital_indices(input_string):
    capital_indices = []
    for index, char in enumerate(input_string):
        if char.isupper():
            capital_indices.append(index)
    return capital_indices

input_string = input()
capital_indices = find_capital_indices(input_string)
print(capital_indices)