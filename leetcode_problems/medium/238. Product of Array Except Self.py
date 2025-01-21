# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """

#         new = []
#         for x in range(len(nums)):
            
#             product = 1
#             for y in range(len(nums)):
                
#                 if not y==x:
#                     product *= nums[y]
#             new.append(product)

#         return new

# this code get time limit exceed for O(n2) complexity


nums = [1,2,3,4]
n = len(nums)
result = [1] * n

# print(result)
prefix = 1
for i in range(len(nums)):
    result[i] = prefix
    prefix *= nums[i]

print(result)
    

