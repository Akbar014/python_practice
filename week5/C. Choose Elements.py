

a, k = list(map(int,input().split()))

myArray = list(map(int,input().split()))

# myArray.sort()
myArray.sort(reverse=True)

result_sum = 0

for i in range(k):
    if(myArray[i] > 0):
        result_sum += myArray[i]

print(result_sum)