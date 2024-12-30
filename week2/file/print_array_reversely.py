

n = int(input("Enter a number : "))

values = list(map(int,input("Enter array elements : ").split()))

for i in range(len(values)-1,-1,-1):
    print(values[i], end=" ")




