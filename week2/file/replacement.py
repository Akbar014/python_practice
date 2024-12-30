

n = int(input("Enter a number : "))

# ar = []

values = list(map(int,input("Enter array elements : ").split()))


for i in range(len(values)):
    if( values[i] > 0):
        values[i] = 1
    elif(values[i]< 0):
        values[i] = 2
    else:
        values[i] = 0


# print(values)
for i in range(len(values)):
    print(values[i], end=" ")


