number = int(input("Enter the value of a : "))

a = number//10
b = number%10
print(a,b)
 

if a%b==0:
    print("YES")
else:
    print("NO")