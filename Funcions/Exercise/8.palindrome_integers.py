def palindrome_integers(number):
    if number == number[::-1]:
        return True
    return False


list_num = input().split(", ")
for current_num in list_num:
    print(palindrome_integers(current_num))