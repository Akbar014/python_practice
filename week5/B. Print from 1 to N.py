
n = int (input())

def print_recursion(n):
    if(n==0):
        return
    
    print_recursion(n-1)
    print(n)

print_recursion(n)
    