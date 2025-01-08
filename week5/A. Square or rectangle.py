

t = int(input())

while t>0 :
    a,b = list(map(int,input().split()))
    if(a==b):
        print("Square")
    else:
        print("Rectangle")
    t -= 1