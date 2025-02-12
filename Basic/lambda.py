

# x = lambda a, b : a * b
# print(x(5, 6))

# y = lambda a,b,c : a+b+c
# print(y(2,3,4))



def my_function(n):
    # x = lambda a : a*2
    # return x
    return lambda n : n*2


myvar = my_function()
print(myvar)
print(myvar(5))


# def myfunc(n):
#   return lambda a : a * n

# mydoubler = myfunc(2)

# print(mydoubler(11))

