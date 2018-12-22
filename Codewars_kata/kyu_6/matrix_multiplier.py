def getMatrixProduct(A, B):
    if len(A[0]) != len(B):
        return -1 
    new_matrix = []
    for pos_rowA in range(0, len(A)):
        new_row = []
        for pos_columnB in range(0, len(B[0])):
            c = 0
            for pos in range(0, len(A[0])):
                c += A[pos_rowA][pos] * B[pos][pos_columnB]

            new_row.append(c)
        new_matrix.append(new_row)
    return new_matrix

if __name__ == "__main__":
    
    assert getMatrixProduct([[2]], [[3]]) == [[6]]
    assert getMatrixProduct([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]]
    assert getMatrixProduct([[0.5, 1],[1.5, 2]], [[0.2, 0.4], [0.6, 0.8]]) == [[0.7, 1.0], [1.5, 2.2]]