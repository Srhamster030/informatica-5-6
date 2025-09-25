def sum_of_row(matrix, row_number: int): #defining what do we want to do 
    row = matrix[row_number]
    row_sum = 0
    for item in row:
        # row_sum = row_sum + item // Example: 0 +5 = 5+6 = 11+7 = 18
        row_sum += item #/it is the same than la de arriba xd

    return row_sum

def sum_of_colum(matrix, column_number: int): #we expect a matrix an we expect an interger.
    column_sum = 0
    for row in matrix: #for every row
        column_sum = column_sum + row[column_number] # add to the row in index x
    return column_sum

def change_value(matrix, row_number, column_number, new_value):
    row = matrix([row_number])
    row[column_number] = new_value 
m = [[4, 2, 3, 2], [9, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]
#my_sum = sum_of_row(m, 1)
# my_sum = sum_of_row(m, 2)
# print(m[2][3]) // "row 2, column 3"

print(m)
change_value(m,2,3,1000)
print(m)
