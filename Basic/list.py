
# thislist = ["apple", "banana", "cherry", "apple", "cherry"]

# print(thislist)
# print(len(thislist))
# print(thislist[3])

# list1 = ["abc", 34, True, 40, "male"]
# print(type(list1))

thislist = list(("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"))
# thislist.insert(2, "watermelon")
thislist.append("last appended")
# tropical = ["mango", "pineapple", "papaya"]
tropical = ("mango", "Orange")
thislist.extend(tropical)
thislist[9] = "updated Orange"


thislist.remove("cherry")
thislist.pop(1)
thislist.pop()   # remove last item 
del thislist[1] 
print(thislist)

# del thislist
thislist.clear()

print(thislist)


print(len(thislist))

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

print(thislist)

# if "apple" in thislist:
#     print("yes, \'apple\' is in the list ")
#     # print("yes, 'apple' is in the list ")
# else:
#     print("Not in the list")
