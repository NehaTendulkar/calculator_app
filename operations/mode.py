from collections import Counter

def calculate_mode(a, b):
    """
    Calculate the mode from a, b, and any additional user-entered numbers.
    """
    numbers = [a, b]

    while True:
        more = input("Add more numbers for mode? (y/n): ")
        if more.lower() == 'y':
            try:
                num = float(input("Enter another number: "))
                numbers.append(num)
            except ValueError:
                print("Invalid number. Please enter a valid numeric value.")
        else:
            break

    frequency = Counter(numbers)
    max_count = max(frequency.values())
    mode = [num for num, count in frequency.items() if count == max_count]

    if len(mode) == len(frequency):
        return "No mode (all values are unique)"
    return mode
