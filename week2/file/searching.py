

n = int(input("Enter a number : "))

ar = []

values = list(map(int,input("Enter array elements : ").split()))

ar.extend(values)

number = int(input("Enter number which you want to search : "))


# print(type(values))
# print(type(ar))
found = False

for i in range(len(values)):
    if(values[i]==number):
        print(i)
        found = True


if not found:
    print(-1)


# for i in range(len(ar)):
#     if(ar[i]==number):
#         print(i)

# for i in range(len(ar)):
#     print(ar[i])