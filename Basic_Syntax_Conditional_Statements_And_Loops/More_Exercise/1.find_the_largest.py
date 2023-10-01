def largest_number_from_digits(number):
    num_str = str(number)
    sorted_digits = sorted(num_str)
    largest_arrangement = ''.join(sorted_digits[::-1])
    largest_number = int(largest_arrangement)
    return largest_number
given_number = int(input())
largest = largest_number_from_digits(given_number)
print(largest)