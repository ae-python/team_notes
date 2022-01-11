def rotate_matrix_90deg(mat):
    row_len = len(mat)
    col_len = len(mat[0])
    result = [[0] * row_len for _ in range(col_len)]
    for r in range(row_len):
        for c in range(col_len):
            # row_len : row_len is real length of row, row_len - 1 : convert to index for list
            result[c][row_len - 1 - r] = mat[r][c]
    return result

# example
# a = [
#     [1, 2, 3, 4],
#     [5, 6, 7, 8],
#     [9, 10, 11, 12]
#     ]

# print(rotate_matrix_90deg(a))