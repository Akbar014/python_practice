

# a = int(input("Enter a non negative value : "))

# if a%2==0:
#     print("even")
# else:
#     print("odd")

while True:
    try:
        num = int(input("Enter a non negative number : "))
        if num > 0:
            if num % 2 == 0:
                print("Even") 
            else:
                print("Odd")
            break
        else:
            print("Invalid input. Please enter a value greater than 0.")
    except ValueError:
        print("Invalid input")
        