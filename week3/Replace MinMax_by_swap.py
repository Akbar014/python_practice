

# n = int(input())

# values = list(map(int, input().split()))
# min = values[0]
# max = values[0]

# for i in range(len(values)):
#     if(values[i] < min):
#         min = values[i]
#     elif(values[i] > max):
#         max = values[i]

# for i in range(len(values)):
#     if(values[i]==min):
#         values[i] = max
#     elif(values[i]==max):
#         values[i] = min


# for i in range(len(values)):
#     print(values[i], end=" ")

# print(min, max)
# print(values)


# ........................................ another soluion ....................................................

n = int(input())

values = list(map(int, input().split()))

min_val = min(values)
max_val = max(values)


values = [max_val if x == min_val else min_val if x == max_val else x for x in values]


# .. explanation for list comprehension  ........................................
new_values = []
for x in values:
    if x == min_val:
        new_values.append(max_val)  # Replace min_val with max_val
    elif x == max_val:
        new_values.append(min_val)  # Replace max_val with min_val
    else:
        new_values.append(x)  # Keep the value unchanged
values = new_values
# .. explanation for list comprehension  ........................................



print(values)





