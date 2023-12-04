def is_valid_input(input_str):
    return (
        input_str.startswith("|") and input_str.endswith("#") and ":" in input_str
    )


def process_input(input_str):
    name_start = input_str.find("|") + 1
    name_end = input_str.find("|", name_start)
    title_start = input_str.find("#") + 1
    title_end = input_str.find("#", title_start)

    boss_name = input_str[name_start:name_end]
    title = input_str[title_start:title_end]

    return boss_name, title


def check_validity(boss_name, title):
    if (
        boss_name.isupper()
        and len(boss_name) >= 4
        and len(title.split()) == 2
        and all(word.isalpha() for word in title.split())
    ):
        return True
    return False


num_inputs = int(input())

for _ in range(num_inputs):
    input_line = input()

    if is_valid_input(input_line):
        boss_name, title = process_input(input_line)

        if check_validity(boss_name, title):
            print(
                f"{boss_name}, The {title}\n>> Strength: {len(boss_name)}\n>> Armor: {len(title)}"
            )
        else:
            print("Access denied!")
    else:
        print("Access denied!")
