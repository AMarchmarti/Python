def finalsudoku(sudoku):
    from esCuadrado import esCuadrado
    from numerosEnRango import numeroEnRango
    from numerosEnFila import numerosEnFila
    from numerosEnColumna import numerosEnColumna
    if esCuadrado(sudoku) and numeroEnRango(sudoku) and numerosEnFila(sudoku) and numerosEnColumna(sudoku):
        return True
    return False

correct = [[1,2,3],
            [2,3,1],
            [3,1,2]]


if finalsudoku(correct):
    print("Es un sudoku")
else: 
    print("No es un sudoku")


incorrect = [[1,2,3,4],
                [2,3,1,3],
                [3,1,2,3],
                [4,4,4,2]]

if finalsudoku(incorrect):
    print("Es un sudoku")
else: 
    print("No es un sudoku")


incorrect2 = [[1,2,3,4],
                [2,3,1,2],
                [4,1,2,3],
                [2,3,1,4]]

if finalsudoku(incorrect2):
    print("Es un sudoku")
else: 
    print("No es un sudoku")


incorrect3 = [[1,2,3,4,5],
                [2,3,1,5,6],
                [4,5,2,1,3],
                [3,4,5,2,1],
                [5,6,4,3,2]]

if finalsudoku(incorrect3):
    print("Es un sudoku")
else: 
    print("No es un sudoku")


incorrect4 = [['a','b','c'],
                ['b','c','a'],
                ['c','a','b']]

if finalsudoku(incorrect4):
    print("Es un sudoku")
else: 
    print("No es un sudoku")


incorrect5 = [ [1, 1.5],
                [1.5, 1]]

if finalsudoku(incorrect5):
    print("Es un sudoku")
else: 
    print("No es un sudoku")


irregular = [[1,2,3],
                [2,3,1]]

if finalsudoku(irregular):
    print("Es un sudoku")
else: 
    print("No es un sudoku")


irregular2 = [[1,2,3],
                [2,3,1],
                [3,1]]

if finalsudoku(irregular2):
    print("Es un sudoku")
else: 
    print("No es un sudoku")