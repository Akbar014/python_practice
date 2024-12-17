
def calculate(a,b):
    sum = a+b
    sub = a-b
    multi = a*b
    div = a/b

    # print(f"{a} + {b} = {sum}")
    # print(f"{a} - {b} = {sub}")
    # print(f"{a} * {b} = {multi}")
    # print(f"{a} / {b} = {div}")

    # print(f"The sum is : {sum}")
    print(a, "+", b, "=", sum)
    print(a, "-", b, "=", sub)
    print(a, "*", b, "=", multi)
    print(f"{a} / {b} = {div:.2f}")
    # print(a, "/", b, "=", {div})


calculate(5,2)