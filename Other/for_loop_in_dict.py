info = {'name': 'Ali', 'age': 28, 'Designation': 'Backend Developer'}

# for key, val in info.items():
#     print(f"{key} : {val}" )

for i,j in enumerate(info.items()):
    # print(i,j)
    print(i,j[0],j[1])

