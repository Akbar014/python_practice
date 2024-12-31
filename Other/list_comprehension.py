
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





