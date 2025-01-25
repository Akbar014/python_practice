
# def my_function():
#     print("Start using function in python")

# my_function()


# def my_function(name):
#     print(f"This is a function with a parameter : {name} ")


# # my_function()
# my_function('test')
# my_function(10)

# x = 10 
# print(f"This is {x}")



# def my_function(fname):
#     print( fname + ' Hossen')


# my_function('akbar')

# def greeting(name):
#     print("Assalamualikum, Welcome " + name)

# greeting('Harun')
# greeting('Mamun')
# greeting('Sumon')



# def my_function(fname, lname):
#     print(fname + " " + lname)


# my_function('sohel', "hossen")


# def my_function(*args):        # Arbitrary Arguments, *args
#     print(type(args))          # Tuple 
#     print("The youngest child is " + args[2])


# my_function('emil','tobias', 'linus')


# def my_function(child1, child2, child3):       # keyword argument
#     print("The youngest child is : " + child3 )

# my_function(child1='emil', child3='tobias', child2='linus')  # keyword argument



# Arbitrary Keyword Arguments, **kwargs
# def my_function(**kwargs):
#     print(kwargs['lname'])

# my_function(fname = 'sohel', lname = 'Hassan')

# def my_function(**kids):
#     print(kids['lname'])

# my_function(fname = 'sohel', lname = 'Hassan')


# def my_function(country = "Norway"):
#   print("I am from " + country)

# my_function("Sweden")
# my_function("India")
# my_function()
# my_function("Brazil")


# def my_function(food):
#     # print(type(food))
#     # print(food)
#     for x in food:
#         print(x)

# fruits = ['apple', 'mango', 'kiwi']
# my_function(fruits)


# def my_function(value):
#     y = str(value)
#     return y

# x = my_function(5)
# print(type(x))


# def my_function(x):
#     return x * 5

# print(my_function(5))
# y = my_function(3)
# z = my_function(4)
# print(y,z)


# def my_function(s1, s2):
#     s3 = s1 + s2
#     # print("Total String: " , s3)   # this is working for both int and string 
#     print("Total String: " + s3) # this only work when s1 and s2 are string otherwise getting error

# my_function('harun', 'patwoary')
# my_function(1,2)


# positional only arguments :

# def fun(a,b, /):
#     print(a,b)

# fun(1,2)
# fun(a=1, b=2)  # keyword arguments not allowrd for positonal only (,/) arguments



# Keywords only arguments :
# def fun(*, a,b):
#     print(a,b)

# fun (a=1,b=2)
# fun (1,2)  # not accepts positional arg for *



# Combine Positional-Only and Keyword-Only

# def fun(a,b,/, *,c,d):
#     print(a,b,c,d)

# fun(1,2, c=3,d=4)


def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)