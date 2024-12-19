import math

def count_divisors(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1 if i == n // i else 2
    return count

print(count_divisors(36))  # Output: 9
