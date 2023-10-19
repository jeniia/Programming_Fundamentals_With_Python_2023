def process_input(input_string, data):
    if input_string == "int":
        print(int(data) * 2)
    elif input_string == "real":
        print(f"{(float(data) * 1.5):.2f}")
    elif input_string == "string":
        print(f"${data}$")


input_string = input()
data_input = input()

process_input(input_string, data_input)