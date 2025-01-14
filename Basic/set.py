
# mySet = {'apple', 'banana', 'cherry'}
# mySet1 = {'apple', 'banana', 'cherry', 'apple'}
# mySet2 = {'apple', 'banana', 'cherry', 'apple', True, 1, 2}   # True and 1 both are same in sets
# mySet3 = {'apple', 'banana', 'cherry', 'apple', False, 0, 2}   # False and 0 both are same in sets

# print(mySet)
# print(mySet1)
# print(mySet2)
# print(mySet3)
# print(len(mySet3))

# thisset = {'apple', 'banana', 'cherry'}
# thisset = {1, 2, 3, 5,7}
# thisset = {True, False, True}
# thisset = {"abc", 34, True, 40, "male"}
thisset = set(('apple', 'banana', 'cherry'))
# print(thisset)

# for x in thisset:
#     print(x)

# print('banana' in thisset)
# print('banana' not in thisset)


# thisset.add("kiwi")
# tropical = {"pineapple", "mango", "papaya"}
# thisset.update(tropical)

# mylist = ["kiwi", "orange"]
# thisset.update(mylist)

# myset = {'kiwi', 'orange'}
# thisset.update(myset)





# thisset.remove('banana')
# thisset.discard('banana')
# thisset.discard('fsd')

# thisset.pop()   # random value reomve
# thisset.clear()

# del thisset
# print(thisset)





# set1 = {'a', 'b', 'c'}
# set2 = {1,2,3}
# set3 = {'john', 'alena'}
# set4 = {'apple', 'banana', 'cherry'}

# myset = set1.union(set2, set3, set4)
# myset = set1 | set2 | set3 | set4


# print(myset)



# set3 = set1.union(set2)
# set3 = set1 | set2


# print(set3)


# x = {'a', 'b', 'c'}
# y = (1, 2, 3)

# # z = x.union(y)
# x.update(y)
# print(x)



set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
# set2 = ('google', 'microsoft', 'apple')

# set3 = set1.intersection(set2)   # can intersect with differecnt data type
# set3 = set1 & set2            # must have same data type
# print(set3)


# set1.intersection_update(set2)
# set1 &= set2

# print(set1)
# print(set3)



# set3 = set1.difference(set2)
# set3 = set1 - set2  
# set1.difference_update(set2)
# set3 = set1.symmetric_difference(set2)    # which elements are not present in the both sets
# set3 = set1 ^ set2
# set1.symmetric_difference_update(set2)

print(set3)