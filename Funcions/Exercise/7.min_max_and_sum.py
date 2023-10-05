list_num = [int(x) for x in input().split()]


for num in list_num:
    minimum_num = min(list_num)
    maximum_num = max(list_num)
    sum_numbers = sum(list_num)


print(f"The minimum number is {minimum_num}")
print(f"The maximum number is {maximum_num}")
print(f"The sum number is: {sum_numbers}")