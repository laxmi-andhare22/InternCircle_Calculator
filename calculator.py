def get_valid_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a number.")

def basic_calculator():
    print("\n--- Basic Calculator ---")
    print("1. Add (+)  2. Subtract (-)  3. Multiply (*)  4. Divide (/)")
    
    while True:
        choice = input("Choose operation (1-4): ")
        if choice in ['1','2','3','4']:
            break
        print("Invalid choice! Enter 1 to 4.")

    num1 = get_valid_number("Enter first number: ")
    num2 = get_valid_number("Enter second number: ")

    if choice == '1':
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif choice == '2':
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif choice == '3':
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif choice == '4':
        while num2 == 0:
            print("Cannot divide by zero!")
            num2 = get_valid_number("Enter second number again: ")
        print(f