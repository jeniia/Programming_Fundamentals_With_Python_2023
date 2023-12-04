def spellcasting(spell, commands):
    current_spell = spell

    for command in commands:
        if command == "Abracadabra":
            break

        parts = command.split()

        if parts[0] == "Abjuration":
            current_spell = current_spell.upper()
            print(current_spell)
        elif parts[0] == "Necromancy":
            current_spell = current_spell.lower()
            print(current_spell)
        elif parts[0] == "Illusion":
            index = int(parts[1])
            letter = parts[2]

            if 0 <= index < len(current_spell):
                current_spell = current_spell[:index] + letter + current_spell[index + 1:]
                print("Done!")
            else:
                print("The spell was too weak.")
        elif parts[0] == "Divination":
            first_substring = parts[1]
            second_substring = parts[2]

            if first_substring in current_spell:
                current_spell = current_spell.replace(first_substring, second_substring)
                print(current_spell)
            else:
                print("The spell did not work!")
        elif parts[0] == "Alteration":
            substring = parts[1]

            if substring in current_spell:
                current_spell = current_spell.replace(substring, "")
                print(current_spell)
            else:
                print("The spell did not work!")
        else:
            print("The spell did not work!")

spell = input()
commands = []
while True:
    command = input()
    commands.append(command)
    if command == "Abracadabra":
        break

spellcasting(spell, commands[:-1])
