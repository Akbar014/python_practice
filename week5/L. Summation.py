
n = int (input())
myList = list(map(int,input().split()))

def get_sum(index, myList):

    if index<0:
        return 0

    return myList[index] +  get_sum(index-1,myList)

print(get_sum(n-1, myList))
    