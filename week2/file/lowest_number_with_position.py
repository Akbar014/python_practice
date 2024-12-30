
n = int(input("Enter array size : "))

values = list(map(int,input("Enter array elements : ").split()))

lowest = values[0]
index = 0

for i in range(len(values)):
    if(values[i] < lowest):
        lowest = values[i]
        index = i+1


print(lowest, index)