'''Python program to reverse a string using exception handling'''


def reverse():
    try:
        # Getting the string from the user input
        myStr = str(input("Enter string: "))

        # Check if the input is empty
        if not myStr:
            raise ValueError("Input string cannot be empty.")

        rev = ""
        for i in myStr:
            rev = i + rev

        print("Reversed String:", rev)

        # Check if the string is a palindrome
        if myStr == rev:
            print(f"String '{myStr}' is a palindrome")
        else:
            print(f"String '{myStr}' is not a palindrome")

    except ValueError as ve:
        print(f"Error: {ve}")
    except TypeError as te:
        print(f"Error: {te}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Execution of the reverse function completed.")


# Calling the function
reverse()

'''python program to handle division by zero'''


def divide(num1, num2):
    try:
        result = num1/num2
        print(f"The result of {num1} divided by {num2} is: {result}")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
    finally:
        print("code got executed successfully.")


divide(int(input("Enter number 1:")), int(input("Enter number 2:")))


'''python program to Catch Invalid Type Error'''


def Addition(a, b):
    try:
        result = a+b
        print(f"The result of {a} plus {b} is :{result}")

    except TypeError:
        print("Error: Both the numbers should be of same datatype.")

    finally:
        print("Program Executed successfully.")


Addition(1, 'a')

'''python program to handle indexerror.'''


def myList(mylist, index):
    try:
        element = mylist[index]
        print(f"The element at index {index} is {element}.")

    except IndexError:
        print("Error: index is out of range.")

    finally:
        print("Code Executed successfully.")


myList([1, 2, 3, 4, 5,], 2)


'''python program to handle value error'''


def handleValueError(num):
    try:
        result = int(num)
        print(f"The value you enter is {result}")

    except ValueError:
        print("Entered value is not valid.")


handleValueError("abc")


'''python program to handle error handling using exception'''


def tableOfNumber(num):
    try:

        print(f"Multiplication table for  is :")
        for i in range(1, 11):
            result = num*i
            print(f"{num}*{i}={result}")
        print("Code executon is successful")
    except ValueError:
        print(f"Enter a valid integer.")

    except Exception as e:
        print(f"An error {e} occured.")


tableOfNumber(int(input("Enter the number whose table you want to print:")))


'''attribute error handling'''


class userDetails:
    def __init__(self, userName, userEmail, userAddress=None, userMobileNumber=None):
        self.userName = userName
        self.userEmail = userEmail
        self.userAddress = userAddress
        self.userMobileNumber = userMobileNumber
        pass

    def printUserEmail(self):
        try:
            print(f"User email is : {self.userEmail}")
        except AttributeError:
            print(f"{self.userName} does not have email.")

    def printuserAdress(self):
        try:
            print(f"User address is : {self.userAddress}")
        except AttributeError:
            print(f"{self.userName} does not have address")

    def AttributeError(self):
        try:
            print(f"User address is : {self.AttributeError}")
        except AttributeError:
            print(f"{self.userName} attribute is not present in class")
