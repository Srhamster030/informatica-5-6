def sum_of_row(matrix, row_number: int):
    row = matrix[row_number]
    row_sum = 0
    for item in row:
        # row_sum = row_sum + item // Example: 0 +5 = 5+6 = 11+7 = 18
        row_sum += item #/it is the same than la de arriba xd

    return row_sum

def sum_of_colum(matrix, colum_number: int):
    column_sum = 0
    for row in matrix:
        colum_sum = colum_sum + row[colum_number]
    return column_sum

m = [[4, 2, 3, 2], [9, 12, 11], [7, 8, 9, 5], [2, 9, 15, 1]]
my_sum = sum_of_row(m, 2)
print(my_sum)
