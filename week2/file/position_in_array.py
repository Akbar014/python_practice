

n = int(input("Enter a number : "))

values = list(map(int,input("Enter array elements : ").split()))

for i in range(len(values)):
    if(values[i] <= 10):
        # print("A[",i,"] = ", values[i])
        print(f"A[{i}]={values[i]}")


