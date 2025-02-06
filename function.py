# def sum():
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     return a + b
# print(sum())


# def multiply(a,b):
#     return a*b
# c = int(input("Enter first number: "))
# d = int(input("Enter second number: "))
# print(multiply(c,d))

#insertion into list by taking user input
# myList = []
# elements = int(input("Enter the number of elements you want to enter into the list: "))
# for i in range(elements):
#     myList.append(input(f"enter element you want at index {i}: "))

# print(myList)

#Insertion into list using function
# myList=[]
# limit = int(input("Enter the limit of elements: "))
# def insertion():
#     if len(myList)<limit:
#         myList.append(input("Enter the elements:"))
#         insertion() 
#     return myList     
# print(insertion())        

#star pattern
# def star():
#     num=int(input("Enter the digit upto which the star should be printed: "))
#     for i in range(0,num+1):
#         print(" "*num,i * "*")
#         num-=1
# star()        

# Positional Arguments
# def add(a,b):
#     return a+b

# result = add(3,5)
# print(result)

# #keywords Arguments
# def add(a,b):
#     return a+b

# result = add(b=5,a=4)
# print(result)

#default 
def multiply(a,b=5):
    return a*b
print(multiply(int(input("Enter number: "))))
                                                         







