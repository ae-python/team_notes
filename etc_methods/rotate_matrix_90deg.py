def rotate_matrix_90deg(mat):
    row_len = len(mat)
    col_len = len(mat[0])
    result = [[0] * row_len for _ in range(col_len)]
    for r in range(row_len):
        for c in range(col_len):
            result[c][row_len - 1 - r] = mat[r][c]
    return result
