
n = int (input())

def print_recursion(n):
    if(n==0):
        return
    print(n, end=" ") 
    print_recursion(n-1)
    

print_recursion(n)
    