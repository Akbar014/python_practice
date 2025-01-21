
nums = [1,2,3,4]
new = []
for x in range(len(nums)):
    # print(x)
    product = 1
    for y in range(len(nums)):
        # print(y)
        if not y==x:
            product *= nums[y]
    new.append(product)

print(new)
