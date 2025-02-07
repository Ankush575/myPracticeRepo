#program to find the factorial of a number using function
num = int(input("Enter the number: "))
def factorial():
   x=1
   for i in range(1,num+1):
      x = x*i
   print(x)     

factorial()        


#program to find the factorial using recursion
n=int(input("ENter the number: "))
def fact(n):
    if n<=1:
        return n
    return n*fact(n-1)
print(fact(n))


#program to reverse a string and check that string is palindrome or not
myStr = str(input("Enter string: "))

def reverse():
    rev =""
    for i in myStr:
        rev = i + rev
    print(rev)
    if myStr==rev:
        print(f"string {myStr} is a palindrome")
    else:
        print(f"string {myStr} is not palindrome")    
reverse()        

#program that takes input from the user  as five digit number and gives the sum of those numbers
num = input("Enter the five digit number: ")
sum = 0
if len(num)<5:
    print(f"Length of number {num} is less than 5")
elif len(num)>5:
    print(f"Number {num} exceeds the limit.")    
else:    
 for i in range(len(num)):
    sum = int(num[i]) + sum
 print(f"The sum of the number {num} is:",sum)

#program to print the fibonacci series using function
def fibb(limit):
    l=[0,1]
    for i in range(limit):
        l.append(l[-1]+l[-2])
    print(l)  
fibb(int(input("Enter the number of limit:")))      


#program to print the position of the element in  fibonacci series using recursion
n=int(input("ENTER YOUR NUMBER HERE: "))
def fib(n):
    if n<=1:
        return n
    return fib(n-1)+fib(n-2)
print(fib(n))
   
#pyhton program to check number is prime or not
def is_prime_recursive(n, i=2):
    
    if n <= 1:
        return False
 
    if n % i == 0:
        return False
    
    if i > n // 2:
        return True
    
    return is_prime_recursive(n, i + 1)

n = int(input("Enter a number: "))
if is_prime_recursive(n):
    print(f"{n} is a prime number.")
else:
    print(f"{n} is not a prime number.")

#program to check that number is palindrome or not 
def palindrome(n):
    rev = ""
    for i in n:
        rev = i+rev
    print(rev)

    if rev ==n:
        print(f"number {n} is a palindrome number.")
    else:
        print(f"number {n} is not a palindrome number.")

palindrome((input("Enter the number: ")))



    

    






   