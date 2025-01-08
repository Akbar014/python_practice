
rows,cols = list(map(int,input().split()))

# cols = int(input())
matrix = []
# print(rows)
# print(cols)

for _ in range(rows):
    row = list(map(int, input().split()))  
    matrix.append(row)

n = int(input())

found = False

for i in range(rows):
    for j in range(cols):
        if(matrix[i][j] == n):
            found = True
    # primary_diagonal_sum += matrix[i][i]
    # print(matrix[i][i], end=" ")

if(found):
    print("will not take number")
else:
    print("will take number")

    
# for i in range(rows):
#     secondary_diagonal_sum += matrix[i][rows-i-1]

# result = abs(primary_diagonal_sum - secondary_diagonal_sum)
# print(result)


