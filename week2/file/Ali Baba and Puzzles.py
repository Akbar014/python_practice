
a = int(input("Enter the value of a : "))
b = int(input("Enter the value of b : "))
c = int(input("Enter the value of c : "))
d = int(input("Enter the value of d : "))

if(a+b-c==d):
    print("YES")
elif(a-b+c == d):
    print("YES")
elif(a+b*c == d):
    print("YES")
elif(a*b+c == d):
    print("YES")
elif(a-b*c == d):
    print("YES")
elif(a*b-c == d):
    print("YES")
else:
    print("NO")