
# thistuple = ('apple', 'banana', 'cherry')
# thistuple1 = (1,2,3)
# thistuple2 = (True, True, False)
# thistuple3 = ('apple',)    # comma (,) is must for single element tuple
# thistuple4 = ('Akbar', 24, "Software Engineer", 34, True, 40, "male")

# thistuple5 = tuple(('apple', 'banana',34, True, 40, "male"))
# print(type(thistuple))
# print(len(thistuple))
# print(thistuple)
# print(thistuple[1])

# print(thistuple4)
# print(thistuple4[1])

# print(thistuple5)


# tuple access procedure are same as list


# tuple update value by using list 

# x = ('apple', 'banana', 'cherry')
# y = list(x)
# y[1] = 'kiwi'
# y[1] = "kiwi"
# x = tuple(y)
# print(x)

# del x
# print(x)


# fruits = ('apple', 'banana', "cherry")


# (green, yellow, red) = fruits
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)


# fruits = ('apple', 'banana', "cherry", 'strawberry', 'raspberry')
# # (green, yellow, *red) = fruits   # using asterisk*
# (green, *yellow, red) = fruits   # using asterisk*
# print(green)
# print(yellow)
# print(red)


# fruits =  ('apple', 'banana', 'cherry')
# i= 0
# while i < len(fruits):
#     print(fruits[i])
#     i += 1

# for x in fruits:
#     print(x)


# for i in range(len(fruits)):
#     print(fruits[i]) 


# thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

# x = thistuple.count(5)

# print(x)


thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)

x = thistuple.index(8)

print(x)




# tuple1 = ("a", "b" , "c")
# tuple2 = (1, 2, 3)

# tuple3 = tuple1 + tuple2
# print(tuple3)


# fruits = ("apple", "banana", "cherry")
# mytuple = fruits * 2

# print(mytuple)