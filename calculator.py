# Simple Calculator

# Addition ( + )
def add(a, b):
    return a + b

# Subtraction ( - )


def subtract(a, b):
    return a - b

# Multiplication ( * )


def multiply(a, b):
    return a * b

# Division ( / )


def divide(a, b):
    if b == 0:
        return "Error! Division by zero."
    return a / b


def calculator():
    print("======= Simple Calculator =======")
    print("Select operation:")
    print("1. Add (+)")
    print("2. Subtract (-)")
    print("3. Multiply (*)")
    print("4. Divide (/)")
    print("5. Quit")
    print("=================================")

    while True:
        choice = input("\nEnter choice (1/2/3/4) or '5' to quit: ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"Result: {add(num1, num2)}")
            elif choice == '2':
                print(f"Result: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Result: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Result: {divide(num1, num2)}")

        elif choice.lower() == '5':
            print("Exiting the calculator. Goodbye!")
            break

        else:
            print("Invalid input. Please select a valid operation.")


if __name__ == "__main__":
    calculator()
