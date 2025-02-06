###################List############################

a = [1,2,3,4,"phone"] 
for i in a:
    print(i)

#del keyword
a = [1,2,3,4,5,6]
del a[1]
print(a)

#remove method
a = [1, 2, 3, 2, 3, 4, 5]
a.remove(3)
print(a)

#pop method
a = [1,4,5,3,2,4,6,1,"string"]
a.pop()
print(a)

#insert 
a = [10, 20 , 30, 40, 50 ]
a.insert(2,60)
print(a)

# #append
a = [10, 20 , 30, 40, 50 ]
a.append(34)
print(a)

#slicing
a = [10, 20 , 30, 40, 50 ]
a=a[0:2]
print(a)

#sort method
a = [10, 20 , 5,2, 40, 50 ]
a.sort()
print(a)

#conversion of list into tuple or to other data structures
a = [23,45,56,23]
tup = set(a)
print(type(tup))

################Dictionary####################
myDict = {
    "name":"jon Doe",
    "age" :20
}

#addition of new key value pair
myDict["class"] = "first"
print(myDict)

#updation of existing key value pair
myDict["name"] = "jon snow"
print(myDict)

for key, value in myDict.items():
    print(f"{key}:{value}")

# Iterating over the dictionary using items()
print("Iterating over dictionary:")
for key, value in myDict.items():
    print(f"{key}: {value}")


###############Tuple########################
#creation of tuple
tup1 = (1,2,34,5,6,7)
tup2 = (23,65,7,3)
tup3 = tup1 + tup2
print(tup3)

# Length of a tuple
tuple_length = len(tup1)
print("Length of tuple:", tuple_length) 

# Nested tuple
nested_tuple = (1, 2, (3, 4))
print("Nested tuple:", nested_tuple) 
print("Accessing nested tuple:", nested_tuple[2])  


############Set################
# Creating a set
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)

# Removing an element using remove()
my_set.remove(4)
print("After removing 4:", my_set)

# Removing an element using discard() (doesn't raise error if element doesn't exist)
my_set.discard(7)  
print("After discard 7 (not present):", my_set)

# Removing an element using pop()
removed_element = my_set.pop()
print("Removed element using pop():", removed_element)
print("After pop:", my_set)



