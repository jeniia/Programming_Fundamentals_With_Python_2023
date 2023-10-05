def total_sum(all_number):
    total_even = 0
    total_odd = 0
    for num in all_number:
        num = int(num)
        if num % 2 == 0:
            total_even += num
        else:
            total_odd += num
    return f"Odd sum = {total_odd}, Even sum = {total_even}"


number = input()
print(total_sum(number))