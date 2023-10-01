def calculate_order_price(price_per_capsule, days, capsules_needed_per_day):
    if (
        0.01 <= price_per_capsule <= 100.00
        and 1 <= days <= 31
        and 1 <= capsules_needed_per_day <= 2000
    ):
        total_price = price_per_capsule * days * capsules_needed_per_day
        return total_price
    else:
        return None

def main():
    n = int(input())
    total_price = 0

    for _ in range(n):
        price_per_capsule = float(input())
        days = int(input())
        capsules_needed_per_day = int(input())

        order_price = calculate_order_price(
            price_per_capsule, days, capsules_needed_per_day
        )

        if order_price is not None:
            print(f"The price for the coffee is: ${order_price:.2f}")
            total_price += order_price

    print(f"Total: ${total_price:.2f}")

if __name__ == "__main__":
    main()
