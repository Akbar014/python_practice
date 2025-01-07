
n = int (input())

def print_recursion(n):
    if(n==0):
        return
    
    print_recursion(n-1)
    print("I love Recursion")

print_recursion(n)
    