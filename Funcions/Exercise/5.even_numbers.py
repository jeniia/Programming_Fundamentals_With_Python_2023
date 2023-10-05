def filter_even_numbers(numbers):
    return list(filter(lambda x: x % 2 == 0, numbers))


def main():
    input_numbers = input()
    numbers = list(map(int, input_numbers.split()))

    even_numbers = filter_even_numbers(numbers)

    print(even_numbers)


if __name__ == "__main__":
    main()