while True:
    print("CALCULATOR BY USING PYTHON")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("Choose operation:")
    print("1 for Addition")
    print("2 for Subtraction")
    print("3 for Multiplication")
    print("4 for Division")
    print("5 for Exit")

    choice = int(input("Enter the operation key (1 to 5): "))

    if choice == 5:
        print("Exiting the calculator. Goodbye!")
        break  # Exit the loop

    if choice in range(1, 5):
        if choice == 1:
            print("Addition is:", num1 + num2)

        elif choice == 2:
            print("Subtraction is:", num1 - num2)

        elif choice == 3:
            print("Multiplication is:", num1 * num2)

        elif choice == 4:
            if num2 != 0:
                print("Division is:", num1 / num2)
            else:
                print("Error: Division by zero")

    else:
        print("Please enter a valid input (1 to 5) to perform the calculation.")
