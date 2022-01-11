def rotate_matrix_90deg(mat):
    row_len = len(mat)
    col_len = len(mat[0])
    result = [[0] * row_len for _ in range(col_len)]
    for r in range(row_len):
        for c in range(col_len):
            # row_len : row_len is real length of row, row_len - 1 : convert to index for list
            result[c][row_len - 1 - r] = mat[r][c]
    return result

def rotate_matrix_180deg(mat):
    row_len = len(mat)
    col_len = len(mat[0])
    result = [[0] * col_len for _ in range(row_len)]
    for r in range(row_len):
        for c in range(col_len):
            result[row_len - 1 - r][col_len - 1 - c] = mat[r][c]
    return result

def rotate_matrix_270deg(mat):
    row_len = len(mat)
    col_len = len(mat[0])
    result = [[0] * row_len for _ in range(col_len)]
    for r in range(row_len):
        for c in range(col_len):
            result[col_len - 1 - c][r] = mat[r][c]
    return result