
n = int (input())
myList = list(map(int,input().split()))


def print_recursion(n, myList):
    if(n<0):
        return 

    if(n%2==0):
        print(myList[n], end=" ") 
        
    print_recursion(n-1,myList)
    

print_recursion(n-1, myList)
    