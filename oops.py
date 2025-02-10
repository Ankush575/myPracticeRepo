'''Python program to crearte a simple program using the concept of object and classes.'''
# Creation of the class


class Dog:
    species = "bullDog"

    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass


# Creating of the object of the Dog class
dog = Dog(input("Enter the Dog name: "), int(
    input("Enter the age of the dog: ")))

print(
    f"The name of the dog is {dog.name}, its age is {dog.age} and species is {dog.species}.")


'''program using single inheritance'''
'''In single inheritance, a subclass inherits from one superclass.'''


class Animal:
    numberOfLegs = 4

    def __init__(self, species):
        self.species = species
        pass

# inherited class


class Dog(Animal):
    def __init__(self, species, age, color, name):
        super().__init__(species)
        self.name = name
        self.age = age
        self.color = color


# creation of objects for both the classes
animal = Animal(input("Enter the species of the animal: "))
dog = Dog(input("Enter the species of the dog :"), int(input("Enter the age of dog :")),
          input("Enter the color of the dog: "), input("Enter the name of the dog :"))

# printing the output
print(
    f"The species of the animal is {animal.species} and it has {animal.numberOfLegs} legs.")
print(
    f"The name of the dog is {dog.name}, its age is {dog.age} and color is {dog.color}.")

'''program using multiple inheritance'''
'''In multiple inheritance, a subclass can inherit from more than one class.'''


class Vehicle:
    def __init__(self):
        self.vehicleCategory = input(
            "Enter your vehicle category (2-wheeler or 4-wheeler):")
        print(f"You entered {self.vehicleCategory} as your vehicle category.")
        pass


class Fuel:
    def __init__(self):
        self.fuelType = input(
            "Enter your vehicle's fuel type(diesel or petrol):")
        print(f"You entered {self.fuelType} as your vehicle category.")
        pass


class tollTax(Vehicle, Fuel):
    def __init__(self):
        Vehicle.__init__(self)
        Fuel.__init__(self)

        if self.vehicleCategory == "2-wheeler":
            if self.fuelType == "petrol":
                self.tax = 10
            else:
                self.tax = 8

        elif self.vehicleCategory == "4-wheeler":
            if self.fuelType == "diesel":
                self.tax = 20
            else:
                self.tax = 18
        else:
            self.tax = 0

        print(f"The toll tax for your vehicle is: {self.tax}")


vehicleAndFuel = tollTax()


'''program using multilevel inheritance'''
'''In multilevel inheritance, a class derives from a class that is already derived from another class.'''


class Education:
    def __init__(self):
        self.education = input("Enter the level of your education :")
        pass


class Subject(Education):
    def __init__(self):
        super().__init__()
        self.subject = input("Enter your specialized subject: ")
        pass


class Grades(Subject):
    def __init__(self):
        super().__init__()
        self.grade = input("Enter your grade (A,B,C,D):")
        self.resultStatus = input("Enter your result status (pass or fail)")
        pass


grades = Grades()

print(
    f"The education level is {grades.education}, specialized subject is {grades.subject}"
    f" and the grade is {grades.grade}")


'''program of hierarchical inheritance'''
'''In hierarchical inheritance, multiple subclasses inherit from a single superclass.'''


class Animal:
    def __init__(self):
        self.species = input("Enter the species of the animal: ")


class Dog(Animal):
    def __init__(self):
        super().__init__()
        self.name = input("Enter the name of the dog: ")
        self.age = int(input("Enter the age of the dog: "))
        self.color = input("Enter the color of the dog: ")


class Cat(Animal):
    def __init__(self):
        super().__init__()
        self.name = input("Enter the name of the cat: ")
        self.age = int(input("Enter the age of the cat: "))
        self.color = input("Enter the color of the cat: ")


dog = Dog()
cat = Cat()


print(
    f"The name of the dog is {dog.name}, its age is {dog.age}, color is {dog.color}, and species is {dog.species}.")
print(
    f"The name of the cat is {cat.name}, its age is {cat.age}, color is {cat.color}, and species is {cat.species}.")


'''program using hybrid inheritance'''
'''In hybrid inheritance, a class inherits from more than one class.'''


class Animal:
    def __init__(self):
        self.species = input("Enter the species of the animal: ")


class Pet:
    def __init__(self):
        self.name = input("Enter the name of the pet: ")
        self.age = int(input("Enter the age of the pet: "))
        self.color = input("Enter the color of the pet: ")


class Dog(Animal, Pet):
    def __init__(self):
        Animal.__init__(self)
        Pet.__init__(self)


class Cat(Animal, Pet):
    def __init__(self):
        Animal.__init__(self)
        Pet.__init__(self)


dog = Dog()
cat = Cat()

print(
    f"The name of the dog is {dog.name}, its age is {dog.age}, color is {dog.color}, and species is {dog.species}.")
print(
    f"The name of the cat is {cat.name}, its age is {cat.age}, color is {cat.color}, and species is {cat.species}.")


'''Polymorphism is the ability of an object to take on many forms.
This means that we can use a method in multiple ways. It is often achieved through:'''
'''polymorphism with method overriding'''


class Animal:
    def speak(self):
        print("The animal makes a sound")


class Dog(Animal):
    def speak(self):
        print("The dog barks")


class Cat(Animal):
    def speak(self):
        print("The cat meows")


class Cow(Animal):
    def speak(self):
        print("The cow moos")


def animal_sound(animal):
    animal.speak()


dog = Dog()
cat = Cat()
cow = Cow()


animal_sound(dog)
animal_sound(cat)
animal_sound(cow)


'''polymorphism with method overloading'''


class Calculator:

    def add(self, *args):
        if len(args) == 1:

            return args[0]
        elif len(args) == 2:

            return args[0] + args[1]
        elif len(args) == 3:

            return args[0] + args[1] + args[2]
        else:

            return "Method accepts 1, 2, or 3 arguments only."


calc = Calculator()

print(calc.add(5, 10))
print(calc.add(5))
print(calc.add(5, 10, 15))
print(calc.add(1, 2, 3, 4))


'''program of encapsulation'''
'''Encapsulation is the OOP concept of bundling data (attributes) and methods (functions)
that operate on the data into a single unit, usually a class.'''


class bankAccount:
    def __init__(self, accountHolder, balance):
        self.__accountHolder = accountHolder
        self.__balance = balance
        pass

    def getAccountHolder(self):
        return self.__accountHolder

    def getAccoutBalance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")

        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient balance.")


account = bankAccount(input("Enter the name of Account holder:"), float(
    input("Enter the balance amount:")))

print("Account Holder:", account.getAccountHolder())
print("Initial Balance:", account.getAccoutBalance())

account.deposit(float(input("Enter the amount you want to deposit:")))
account.withdraw(float(input("Enter the amount you want to withdraw:")))


'''program of abstraction'''


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


# Using the classes
circle = Circle(float(input("Enter the radius of the circle:")))
rectangle = Rectangle(float(input("Enter width of the rectangle:")), float(
    input("Enter the height of the rectangle:")))

print(f"Area of circle: {circle.area()}")
print(f"Area of rectangle: {rectangle.area()}")


'''program of Special methods (__str__, __repr__).'''


class bankAccount:
    def __init__(self, accountNumber, accountHolder, balance):
        self.accountNumber = accountNumber
        self.accountHolder = accountHolder
        self.balance = balance

    def __str__(self):
        return f"Bank Account of {self.accountHolder} (Account Number: {self.accountNumber}) with balance ${self.balance:.2f}"

    def __repr__(self):
        return f"BankAccount({self.accountNumber}, '{self.accountHolder}', {self.balance})"


account1 = bankAccount(int(input("Enter first Account Number:")), input(
    "Enter first account holder name:"), float(input("Enter the balance amount of first account:")))
account2 = bankAccount(int(input("Enter second account number:")), input(
    "Enter second account holder name:"), float(input("Enter the balance amount of second account: ")))

print(account1)


print(repr(account1))

account2
