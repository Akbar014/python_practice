
# thislist = ["apple", "banana", "cherry", "apple", "cherry"]

# print(thislist)
# print(len(thislist))
# print(thislist[3])

# list1 = ["abc", 34, True, 40, "male"]
# print(type(list1))

thislist = list(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))
# # thislist.insert(2, "watermelon")
# thislist.append("last appended")
# # tropical = ["mango", "pineapple", "papaya"]
# tropical = ("mango", "Orange")
# thislist.extend(tropical)
# thislist[9] = "updated Orange"


# thislist.remove("cherry")
# thislist.pop(1)
# thislist.pop()   # remove last item 
# del thislist[1] 
# print(thislist)

# del thislist
# thislist.clear()

# print(thislist)


# print(len(thislist))

# print(thislist[1])
# print(thislist[-1])
# print(thislist[2:5])
# print(thislist[-2::-2])
# print(thislist[:4])
# print(thislist[2:])
# print(thislist[-4:-1])  # not incluidng first item 
# print(thislist[-4:])    # with last item 

# thislist[0] = "nothing"
# thislist[1:3] = ["updated banana", "Watermelon"]
# thislist[1:5] = ["Watermelon"]

# print(thislist)

# if "apple" in thislist:
#     print("yes, \'apple\' is in the list ")
#     # print("yes, 'apple' is in the list ")
# else:
#     print("Not in the list")



# .............................................. loop in lists ..................................................

thislist = ['apple', 'orange', 'banana']

# for item in thislist:
#     print(item)


# for i in range(len(thislist)):
#     print(thislist[i])


# i = 0
# while i < len(thislist):
#     print(thislist[i])
#     i += 1


# x = [print(item) for item in thislist]

# x = [ item for item in thislist]
# print(x)




# ...................................................  list comprehension  ..............................................

# fruits = ["apple", "banana", "orange", "kiwi", "mango"]

# newlist = [x for x in fruits]

# newlist = []
# for x in fruits:
#     if 'a' in x:
#         newlist.append(x)

# newlist = [x for x in fruits if 'a' in x]
# newlist = [x for x in fruits if not 'a' in x ]
# newlist = [x if 'a' in x else 'b' for x in fruits ]
# newlist = [x for x in fruits if x != "apple"]
# newlist = [x if x != "apple" else "nothing" for x in fruits ]
# newlist = [x.upper() for x in fruits]


# newlist = [x for x in range(10)]
# newlist = [x for x in range(10) if x%2==0]



# fruits.sort()
# fruits.sort(reverse=True)

# print(fruits)



# myList = [10,30,20,15,40]

# myList.sort()
# print(myList)
# myList.sort(reverse=True)
# print(myList)


# def myfunc(n):
#     return abs(n-50)

# thislist = [100, 50, 65, 82, 23]
# thislist.sort(key = myfunc)
# print(thislist)


# thislist = ["banana", "Orange", "Kiwi", "cherry"]
# thislist.sort()
# thislist.sort(key=str.lower)
# thislist.reverse()
# print(thislist)

# myList = thislist.copy()
# myList = list(thislist)

# myList = thislist[:]
# myList = thislist

# print(myList)

# newlist = [1,2,3]
# finalList = thislist + newlist
# print(finalList)




# list1 = ["a", "b", "c", "a"]
# list2 = [1,2,3]

# for x in list2:
#     list1.append(x)

# list1.extend(list2)

# print(list1)


# list1.clear()

# print(list1)

# print(list1.count("a"))
# print(list1.index("a"))


# list1.insert(1,"z")
# list1.remove("a")
# list1.reverse()
# list1.sort()
# print(list1)




