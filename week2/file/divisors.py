
import math

number = int(input("Enter a number : "))
divisors = []

#  complexity O(n)
# for i in range(1,number+1):
#     if(number%i == 0):
#         # print(number//i)
#         divisors.append(i)


# complexity O(ROOT(n))
for i in range(1, int(math.sqrt(number)+1)):
    if(number%i == 0):
        divisors.append(i)
        if (i != number // i ):
            divisors.append(number//i)

divisors.sort()
print (divisors)
    