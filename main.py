
from calculatorPackage import calculator


def main():
    print("Welcome to the Python Calculator!")

    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    print("\nSelect an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Modulus")

    choice = input("Enter your choice (1/2/3/4/5): ")

    if choice == '1':
        print(f"The result is: {calculator.add(num1, num2)}")
    elif choice == '2':
        print(f"The result is: {calculator.subtract(num1, num2)}")
    elif choice == '3':
        print(f"The result is: {calculator.multiply(num1, num2)}")
    elif choice == '4':
        try:
            print(f"The result is: {calculator.divide(num1, num2)}")
        except ValueError as e:
            print(e)
    elif choice == '5':
        print(f"The result is: {calculator.modulus(num1, num2)}")
    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
