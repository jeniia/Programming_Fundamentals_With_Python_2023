def process_commands():
    guests_likes = {}
    unliked_meals = 0
    while True:
        command = input().split("-")

        if command[0] == "Stop":
            break
        action, guest, meal = command[0], command[1], command[2]

        if action == "Like":
            if guest not in guests_likes:
                guests_likes[guest] = [meal]
            elif meal not in guests_likes[guest]:
                guests_likes[guest].append(meal)
        elif action == "Dislike":
            if guest in guests_likes:
                if meal in guests_likes[guest]:
                    guests_likes[guest].remove(meal)
                    unliked_meals += 1
                    print(f"{guest} doesn't like the {meal}.")
                else:
                    print(f"{guest} doesn't have the {meal} in his/her collection.")
            else:
                print(f"{guest} is not at the party.")
    for guest, liked_meals in guests_likes.items():
        print(f"{guest}: {', '.join(liked_meals)}")
    print(f"Unliked meals: {unliked_meals}")


process_commands()
