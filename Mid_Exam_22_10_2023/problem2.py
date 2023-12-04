coffees = input().split()
num_commands = int(input())

for _ in range(num_commands):
    command = input().split()
    action = command[0]

    if action == "Include":
        coffee_to_add = command[1]
        coffees.append(coffee_to_add)
    elif action == "Remove":
        position = command[1]
        count = int(command[2])
        if position == "first":
            coffees = coffees[count:]
        elif position == "last":
            coffees = coffees[:-count]
    elif action == "Prefer":
        index_1 = int(command[1])
        index_2 = int(command[2])
        if 0 <= index_1 < len(coffees) and 0 <= index_2 < len(coffees):
            coffees[index_1], coffees[index_2] = coffees[index_2], coffees[index_1]
    elif action == "Reverse":
        coffees.reverse()
print("Coffees:")
print(" ".join(coffees))