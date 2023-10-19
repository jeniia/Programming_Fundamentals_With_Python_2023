def closest_to_center(x1, y1, x2, y2):
    distance1 = x1 ** 2 + y1 ** 2
    distance2 = x2 ** 2 + y2 ** 2

    if distance1 <= distance2:
        closest_point = (x1, y1)
    else:
        closest_point = (x2, y2)
    formatted_point = "({}, {})".format(int(closest_point[0]), int(closest_point[1]))
    return formatted_point


x1 = input()
y1 = input()
x2 = input()
y2 = input()

result = closest_to_center(x1, y1, x2, y2)
print(result)