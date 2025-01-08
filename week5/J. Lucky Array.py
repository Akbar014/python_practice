

n = int(input())

myArray = list(map(int, input().split()))

frq = {}

# for item in myArray:
#     print(item)
for item in myArray:
    if item in frq:
        frq[item] += 1
    else:
        frq[item] = 1 


# min_key = min(frq, key=frq.get)
# min_key = min((key for key in frq if frq[key] == min(frq.values())))
min_key = min(frq.keys())

min_value = frq[min_key]

# min_key, min_value = min(frq.items(), key=lambda x: x[1])

if(min_value%2==0):
    print("Unlucky")
else:
    print("Lucky")


# print(type(min_key))
# print(min_key)
# # print(min_value)

# print(frq.items())

