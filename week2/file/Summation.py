
n = int(input("Enter a number for array size : "))

ar = []

values = list(map(int, input(f"Enter {n} array elements separated by spaces : ").split()))




# ar.extend(values)
# print(ar)

total_sum = sum(values)
# print(total_sum)

# print(values)

if(total_sum > 0):
    print(total_sum)
else:
    print(total_sum * (-1))

