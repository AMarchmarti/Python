#Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.
#array = [[1,2,3],
#        [4,5,6],
#       [7,8,9]]
#snail(array) #=> [1,2,3,6,9,8,7,4,5]
#For better understanding, please follow the numbers of the next array consecutively:

#array = [[1,2,3],
#         [8,9,4],
#         [7,6,5]]
#snail(array) #=> [1,2,3,4,5,6,7,8,9]


def snail(array):
    expected = []
    start_row = 0
    start_column = 0
    end_row = len(array) - 1
    end_column = len(array) - 1
    if array == [[]]:
        return expected
    while start_row < len(array) - 1 and start_row != end_column:
        column = start_column
        while column <= end_column:
            expected.append(array[start_row][column])
            column = column + 1
        row = start_row
        while row < end_row:
            row = row + 1
            expected.append(array[row][end_column])
        column =end_column - 1
        while column >= start_column:
            expected.append(array[row][column])
            column = column - 1
        if column < start_column:
            column = start_column
        end_row -= 1
        row = end_row
        while row > start_row:
            expected.append(array[row][column])
            row = row - 1
        start_column += 1
        start_row += 1
        end_column -= 1
    if expected.count(array[start_row][end_column]) == 0:
        expected.append(array[start_row][end_column])

    return expected

if __name__ == "__main__":
    
    #CASOS TEST
    array = [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]]
    expected1 = [1, 2, 3,6, 9, 8,7,4, 5]
    assert snail(array) == expected1

    array2 = [[1,2,3],
             [8,9,4],
             [7,6,5]]
    expected2 = [1,2,3,4,5, 6,7,8, 9]
    assert snail(array2) == expected2

    array3 = [[1, 2, 3, 4, 5], 
              [6, 7, 8, 9, 10], 
              [11, 12, 13, 14, 15], 
              [16, 17, 18, 19, 20], 
              [21, 22, 23, 24, 25]]
    expected3 = [1,2,3,4,5,10,15,20,25,24,23,22,21,16,11,6,7,8,9,14,19,18,17,12,13]
    assert snail(array3) == expected3

    array4 = [[]]
    expected4 = []
    assert snail(array4) == expected4

    array5 = [[1, 2, 3, 4, 5, 6], 
              [20, 21, 22, 23, 24, 7], 
              [19, 32, 33, 34, 25, 8], 
              [18, 31, 36, 35, 26, 9], 
              [17, 30, 29, 28, 27, 10], 
              [16, 15, 14, 13, 12, 11]]
    expected5 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]
    assert snail(array5) == expected5