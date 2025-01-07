
rows = int(input())
# cols = int(input())
matrix = []

# for i in range(rows):
#     a= []
#     for j in range(cols):
#         a.append(int(input()))
#     matrix.append(a)


for _ in range(rows):
    row = list(map(int, input().split()))  
    matrix.append(row)

# print(matrix)

primary_diagonal_sum = 0
secondary_diagonal_sum = 0


# for i in range(rows):
#     for j in range(cols): 
#         if(i==j):
#             print(matrix[i][j], end=" ")


for i in range(rows):
    primary_diagonal_sum += matrix[i][i]
    # print(matrix[i][i], end=" ")



# mlist = [[1,2,3,4], [1,2,3,4]]
# print(len(mlist))
# print(len(matrix))

for i in range(rows):
    secondary_diagonal_sum += matrix[i][rows-i-1]
    # print(matrix[i][rows - i -1], end=" ")

result = abs(primary_diagonal_sum - secondary_diagonal_sum)
# print(primary_diagonal_sum)
# print(secondary_diagonal_sum)
print(result)


