sequence_of_strings = input().split()
result = []
for current_word in sequence_of_strings:
    length = len(current_word)
    result += current_word * length

print("".join(result))