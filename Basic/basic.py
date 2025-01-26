

# x,y,z = 1,2,3
# print(x)
# print(y)
# print(z)

# ........................................ ....................................

# x,y,z = 'orange', 'banana', 'apple'

# print(x)
# print(y)
# print(z)

# ........................................ .....................................

# x = y = z = 1
# print(y)

# x = y = z = "Orange"
# print(z)

# fruits = ['orane', 'banana', 'cherry']
# x,y,z = fruits
# print(x)
# print(y)
# print(z)

# x = "Python "
# y = "is "
# z = "awesome"
# print(x, y, z)
# print(x+y+z)


# x = 5
# y = "John"
# # print(x + y)   #  will throw an error for diferent type of variable 
# print(x, y) # this will get output 


# def myfunc():
#   global x
#   x = "fantastic"

# myfunc()

# print("Python is " + x)

# ............................................................... .....................................................
# x = "Awesome"
# def myFunction():
#     # global x
#     x = "Fantastic"
#     print(x)

# myFunction()

# print (x)


# x = range(6)

# print(x)




# python built in data types 
#  str, int, float, complex, list, tuple, range, dict, set, frozenset, bool,  bytes, bytearray, memoryview, NoneType




# ............................................................ .........................................
# x = dict(name="John", age=36)
# x = {'name':'John', 'age':3}

# y = x.values()
# z = x.keys()

# print(x.items())
# print(x['name'])

# print(y)
# print(z)

# print(x["name"])



# ..................................................... ...........................................................

# b = "Hello world"
# print(b[2:5])
# print(b[:5])
# print(b[3:])
# print(b[-5::-2])
# print(b[-5:-2])
# print(b[0:11])


# b = "Hello world"
# print(b[-5::-2])
# print(b[-5::-1])

# b = " Hello- world! "

# print(b.upper())
# print(b.lower())
# print(b.strip())  # remove extra spaces
# print(b.replace("H", "-"))



# b = " Hello- world! "
# b = " Hello, world! "
# print(b.split("-"))
# print(b.split(","))



# a = "Hello"
# b = "World"
# # c = a + b
# c = a + " " + b
# print(c)


# age = 36
# txt = f"My name is John, I am {age}"
# print(txt)

# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)

# txt = "We have to check \"escape\" character here "
# txt = "We have to check \'escape\' character here "
# txt = "We have to \\ check \'escape\' character here "
# txt = "We have to t\b check \'escape\' character here "
# txt = "We have to t\n check \'escape\' character here "
# print(txt)


# string methods 

# capitalize(), casefold(), center(), count(), encode(), endswith(), expandtabs, find(), format(), format_map(), index(), 
# isalnum(), isalpha(), isascii(), isdecimal(), isdigit(), isidentifier(), islower(), isnumeric(), isprintable(), isspace(), 
# istitle(), isupper(), join(), ljust(), lower(), lstrip(), maketrans(), partition(),  replace(), rfind(), rindex(),
# rjust(), rpartition(), rsplit(), rstrip(), split(), swapcase(), title(), translate(), upper(), zfill(),


# x = 200
# print(isinstance(x, int))


# .............................   Python Operator .....................................................

# Arithmetic(+, -, *, /, %, **, //), Assignment(=, +=, -=, *=, /=, %=, //=, **=, &=, |=, ^=, >>=, <<=, :=), 
# Comparison(==, !=, >, <, >=, <=), Logical(and, or, not), Identity(is, is not), Membership(in, not in), Bitwise


# x = 5
# a = x
# b = a



# a = [1,2,3]
# b = [1,2,3]

# if a == b:              # when the values of both the operands are equal,  compare the equality of objects,
#     print("Equal")


"""
The 'is' operator evaluates to true if the variables on either side of the operator point to the same object.
If not, it results in a false evaluation.
"""
# if a is b:            
#     print("True")


# a = 4
# b = 5
# a = 5


# a = (1,2,3)
# b = (1,2,3)

# a = [1,2,3]
# b = [1,2,3]

# a = {}
# b = {}

# a = (1, 2, [3, 4])  # টুপলে mutable ডেটা (লিস্ট) আছে
# b = (1, 2, [3, 4])
# a = 5000
# b = 5000
# print(a is b) 
# print(a == b)



"""
is: মেমরি লোকেশন চেক করে।
==: ভ্যালু বা content চেক করে।

"""


# a = [1, 2, 3]
# b = [1, 2, 3]

# print(a == b)  # True, because the values inside the lists are the same.
# print(a is b)  # False, because `a` and `b` refer to two different objects in memory.

# # But if the values are the same and the objects are the same (interning or singletons):
# x = 1000
# y = 1000
# print(x == y)  # True, values are the same.
# print(x is y)  # False, because integers outside the interning range have separate memory locations.

# z = 5
# w = 5
# print(z == w)  # True, values are the same.
# print(z is w)  # True, because 5 is interned and shares the same memory.
