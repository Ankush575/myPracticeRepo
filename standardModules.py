# python program using os module


import random
import datetime
import math
import os


def createDirectory(dirName):
    try:
        if not os.path.exists(dirName):
            os.mkdir(dirName)
            print(f"Directory {dirName} created successfully.")
    except FileExistsError:
        print("Directory already exists.")

    except Exception as e:
        print(f"Error: {e}")

    finally:
        print("Code executed successfully.")


def createFile(fileName):
    try:
        if not os.path.exists(fileName):
            with open(fileName, 'x'):
                print(f"File {fileName} created successfully.")
        else:
            print("File already exists.")
    except Exception as e:
        print(f"Error: {e}")

    finally:
        print("Code executed successfully.")


def listAllFiles():
    try:
        files = os.listdir()
        for file in files:
            print(file)
    except Exception as e:
        print(f"Error: {e}")

    finally:
        print("Code executed successfully.")


def deleteFile(fileName):
    try:
        if os.path.exists(fileName):
            os.remove(fileName)
            print(f"File {fileName} deleted successfully.")
        else:
            print("File not found.")
    except Exception as e:
        print(f"Error: {e}")


def deleteDirectory(dirName):
    try:
        if os.path.exists(dirName):
            os.rmdir(dirName)
            print(f"Directory {dirName} deleted successfully.")
        else:
            print("Directory not found.")
    except Exception as e:
        print(f"Error: {e}")


createDirectory(input("Enter the directory name you want to create:"))
createFile(input("Enter the file name you want to create:"))
deleteDirectory(input("Enter the directory name you want to delete:"))
deleteFile(input("Enter the file name you want to delete:"))
listAllFiles()


# python program using math module


def areaOfRectangle(length, breath):
    if length <= 0 or breath <= 0:
        raise ValueError("Length and breath should be greater than 0.")
    else:
        area = length * breath

    print(f"Area of the rectangle is: {area}")


areaOfRectangle(float(input("Enter the length of the rectangle:")),
                float(input("Enter the breath of the rectangle:")))


def areaOfCircle(radius):
    if radius <= 0:
        raise ValueError("Radius should be greater than 0")
    else:
        area = math.pi * radius**2
        exactArea = math.ceil(area * 100) / 100
        print(f"Area of the circle is: {exactArea}")


areaOfCircle(float(input("Enter the radius of the circle:")))


def squareRootOfANumber(number):
    try:
        if number < 0:
            raise ValueError("Number should be greater than 0.")
        else:
            result = math.sqrt(number)
            print(f"The square root of {number} is {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


squareRootOfANumber(
    float(input("Enter the number you want to find the square root of:")))


def factorialOfNumber(number):
    try:
        if number < 0:
            raise ValueError("Number must be greater than 0.")
        else:
            result = math.factorial(number)
            print(f"The factorial of {number} is {result}:")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Error: {e}")


factorialOfNumber(
    int(input("Enter the number you want to find the factorial of:")))


# python program using datetime module


def currentDateTime():
    try:
        timeobj = datetime.datetime.now()
        dateobj = datetime.date.today()
        print(f"Today the date is {dateobj} and current time is: {timeobj}")
    except Exception as e:
        print(f"Error: {e}")


currentDateTime()


def calculteDaysFromTodayToSpecificDate(year, month, day):
    try:
        presentDate = datetime.date.today()
        futureDate = datetime.date(year, month, day)
        print(
            f"The number of days between {presentDate} and {futureDate} is: {futureDate-presentDate}")
    except Exception as e:
        print(f"Error: {e}")


calculteDaysFromTodayToSpecificDate(
    int(input("Enter the year:")), int(input("Enter the future month:")), int(input("Enter the future date:")))


# python program using random module


def numberGuessingGame(userGuess):
    try:
        randomNumber = random.randint(1, 5)
        if userGuess == randomNumber:
            print(f"Congratulations! You guessed the right number.")
            numberGuessingGame(userGuess)
        else:
            print(f"Better luck next time, The number was {randomNumber}")

    except Exception as e:
        print(f"Error: {e}")


numberGuessingGame(int(input("Enter the number you want to guess:")))
