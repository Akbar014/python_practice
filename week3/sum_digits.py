
# n = int(input())

# sum = 0

# while n>0 :
#     val = n%10
#     sum += val
#     n //= 10

# print(sum)



n = int(input())

a = input()

# summation = sum(int(digit) for digit in a)
summation = 0

for digit in a:
    summation += int(digit)

# summation = sum(int(digit) for digit in a)

print(summation)
