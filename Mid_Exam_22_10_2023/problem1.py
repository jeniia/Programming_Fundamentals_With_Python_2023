num_cities = int(input())
total_profit = 0

for city_num in range(1, num_cities + 1):
    city_name = input()
    income = float(input())
    expenses = float(input())
    if city_num % 3 == 0 and city_num % 5 == 0:
        income += income * 0.4
    elif city_num % 3 == 0:
        expenses += expenses * 0.5
    elif city_num % 5 == 0:
        income -= income * 0.1
    final_profit = income - expenses
    total_profit += final_profit
    print(f"In {city_name} Burger Bus earned {final_profit:.2f} leva.")

print(f"Burger Bus total profit: {total_profit:.2f} leva.")