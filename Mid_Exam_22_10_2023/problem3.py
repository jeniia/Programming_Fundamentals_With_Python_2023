phones = input().split(", ")
while True:
    command = input().split(" - ")
    action = command[0]

    if action == "End":
        break
    phone = command[1]

    if action == "Add" and phone not in phones:
        phones.append(phone)
    elif action == "Remove" and phone in phones:
        phones.remove(phone)
    elif action == "Bonus phone":
        old_phone, new_phone = phone.split(":")
        if old_phone in phones:
            index = phones.index(old_phone)
            phones.insert(index + 1, new_phone)
    elif action == "Last" and phone in phones:
        phones.remove(phone)
        phones.append(phone)
print(", ".join(phones))