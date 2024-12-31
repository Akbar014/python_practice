
# n = int(input())

# while n >0:
    
#     s = input()

#     if(len(s)>10):
#         print(f"{s[0]}{len(s)-2}{s[len(s)-1]}")
#     else:
#         print(s)
    
#     n -= 1

# ..................................... another way to solve ......................................................

n = int(input())

for _ in range(n):
    s = input()
    # true_expression if condition else false_expression  ( Ternary operatior )
    print(f"{s[0]}{len(s) - 2}{s[-1]}" if len(s) > 10 else s)


# print(len(s))