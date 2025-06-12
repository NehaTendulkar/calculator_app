from operations.add import add
from operations.subtraction import subtract
from operations.multiply import multiply
from operations.divide import divide
from operations.mode import calculate_mode
def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def main():
    print("Welcome to the calculator!")
    print("=== Simple Calculator ===")
    print("Creating merge conflict - A version")

    while True:
        a = get_number("Enter first number (or 'q' to quit): ")
        b = get_number("Enter second number: ")
        op = input("Choose operation (+, -, *, /,mode) or 'q' to quit: ")

        if op.lower() == 'q':
            print("Exiting calculator. Goodbye!")
            break

        if op == "+":
            print("Result:", add(a, b))
        elif op == "-":
            print("Result:", subtract(a, b))
        elif op == "*":
            print("Result:", multiply(a, b))
        elif op == "/":
            try:
                print("Result:", divide(a, b))
            except ZeroDivisionError:
                print("Error: Cannot divide by zero.")

        elif op == "mode":
            print("Mode:", calculate_mode(a, b))

        else:
            print("Invalid operation. Please choose from +, -, *, /.")

        print("-" * 30)

if __name__ == "__main__":
    main()

