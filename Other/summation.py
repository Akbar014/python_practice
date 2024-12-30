







# n = int( input("Enter array size : "))

# ar = []

# sum = 0

# for i in range(n):
#     val = int(input("Enter array elements : "))
#     sum += val
#     ar.append(val)

# for i in ar:
#     print(i)


# for i in range(len(ar)):
#     print(ar[i])


# if(sum > 0):
#     print("The sum is : ", sum)
# else:
#     print("The sum is : ", (sum * (-1)))


# ............................ another solution ...........................................................


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







