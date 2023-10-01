number_people = int(input())
capacity = int(input())
coutses = 0

while number_people > 0:
    if number_people - capacity >= 0:
        number_people -= capacity
        coutses += 1
    else:
        if number_people != 0:
            coutses += 1
            break
print(coutses)