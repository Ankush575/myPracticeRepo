#Q.1 
def sum():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a + b
print(sum())

#Q.2
def multiply(a,b):
    return a*b
c = int(input("Enter first number: "))
d = int(input("Enter second number: "))
print(multiply(c,d))

#Q.3insertion into list by taking user input
myList = []
elements = int(input("Enter the number of elements you want to enter into the list: "))
for i in range(elements):
    myList.append(input(f"enter element you want at index {i}: "))

print(myList)

#Q.4Insertion into list using function
myList=[]
limit = int(input("Enter the limit of elements: "))
def insertion():
    if len(myList)<limit:
        myList.append(input("Enter the elements:"))
        insertion() 
    return myList     
print(insertion())        

#Q.5star pattern
def star():
    num=int(input("Enter the digit upto which the star should be printed: "))
    for i in range(0,num+1):
        print(" "*num,i * "*")
        num-=1
star()        

# # Q.6 Positional Arguments
def add(a,b):
    return a+b

result = add(3,5)
print(result)

# # # Q.7keywords Arguments
def add(a,b):
    return a+b

result = add(b=5,a=4)
print(result)

# #Q.8 default 
def multiply(a,b=5):
    return a*b
print(multiply(int(input("Enter number: ")))) 

# #Q.9 variable
# # Using *args
def sum_numbers(*args):
    return sum(args)

print(sum_numbers(1, 2, 3, 4)) 

# # Using **kwargs
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="New York")

#Q.10lambda function
a=lambda x,y: x+y
print(a(1,2))

#Q.11 Celcius to fahrenheit  using lambda

fahrenheit  = lambda c: (c*(9/5))+32 
print(fahrenheit(float(input('Enter the temp in degree :'))))
                                                         





