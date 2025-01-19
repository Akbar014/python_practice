
# myDict = {
#     'name' : 'akbar',
#     'age' : 24
# }

# print(myDict)
# print(myDict['name'])
# print(len(myDict))


# thisdict = {
#     'brand' : 'ford',
#     "electric" : False,
#     'year' : 1996,
#     'colors' : ['red', 'black', 'white'],
# }


# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }


# thisdict = dict(name = "akbar", age=27, country='bangladesh')

# print(thisdict)
# print(thisdict['name'])


thisdict = {
    'brand' : 'Ford',
    'model' : 'Mustang',
    'year' : 1964
}

# x = thisdict['model']

# print(x)

# x = thisdict.get('model')

# x = thisdict.keys()
# x = thisdict.values()
# x = thisdict.items()
# print(x)


# first_item = next(iter(thisdict.items()))
# last_item = next(reversed(thisdict.items()))
# print(first_item)
# print(last_item)

# items = list(thisdict.items())
# print(items[1])


# if 'model' in thisdict:
#     print("yes")


# thisdict['year'] = 2018
# thisdict.update({'year' : 2020})


# thisdict['add_new'] = 'Test'
# thisdict.update({'add_new' : 'test'})

# thisdict.pop('model')
# thisdict.popitem()   # remove last item from dict
# del thisdict # this will delete the dict so print thisdict raise an error

# thisdict.clear()
# print(thisdict)



# for x in thisdict:
#     print(x)    # print all key names in the dict

# for x in thisdict:
#     print(thisdict[x]) # print all values in the dict



# for x in thisdict.keys():
#     print(x)

# for x in thisdict.values():
#     print(x)

# for x,y in thisdict.items():
#     print(x,y)


# coppied_dict = thisdict.copy()
# coppied_dict = dict(thisdict)
# print(coppied_dict)


# myFamily = {
#     'child1' : {
#         'name' : 'abc',
#         'age' : 24
#     },
#     'child2' : {
#         'name' : 'def',
#         'age' : 12,
#     },
#     'child3' : {
#         'name' : 'xyz',
#         'age' : 30,
#         'education' : {
#             'SSC' : 'PQR School',
#             'result' : 'GPA : 5.00'
#         },
#         'hobby' : 'Reading'
#     }
# }






# child1 = {
#     'name' : 'abc',
#     'age' : 24,
# }

# child2 = {
#     'name' : 'def',
#     'age' : 20,
# }

# child3 = {
#     'name' : 'xyz',
#     'age' : 24
# }

# myFamily = {
#     'child1' : child1,
#     'child2' : child2,
#     'child3' : child3,
# }


# print(myFamily)
# print(myFamily['child2']['name'])

# for x, obj in myFamily.items():
#     print(x)

#     for y in obj:
#         print(y + ':' ,  obj[y])



# x = ('key1', 'key2', 'key3')
# y = 0

# thisdict = dict.fromkeys(x,y)

# print(thisdict)


# car = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "colors" : ['red', 'white', 'blue'],
# }

# x = car.setdefault("model", "Bronco")

# print(x)


