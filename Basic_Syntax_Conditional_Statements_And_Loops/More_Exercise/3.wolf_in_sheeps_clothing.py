def warn_sheep(queue):
    animals = queue.split(", ")
    wolf_index = animals.index('wolf')
    if wolf_index == len(animals) - 1:
        return "Please go away and stop eating my sheep"
    else:
        sheep_to_warn = len(animals) - wolf_index - 1
        return f"Oi! Sheep number {sheep_to_warn}! You are about to be eaten by a wolf!"
input_str = input()
output = warn_sheep(input_str)
print(output)