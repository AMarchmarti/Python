##Finalmente aqui haremos la función para comprobar que no se repitan números en las misma columnas.

def numerosEnColumna(sudoku):
    i = 0
    while i < len(sudoku):
        numerosColumna = []
        for lista in sudoku:
            if len(lista) != len(sudoku):#Es una pequeña comprobación para que no nos haga error
                return False
            numerosColumna.append(lista[i])#Este While lo que hace es guardar cada columna en una misma lista.
        i = i + 1
    for numero in numerosColumna:
        if numerosColumna.count(numero) > 1:# Aqui al igua que en las filas, es la comprobación que no se repitan los números.
            return False  
    return True
    
                    


#Casos Tests: comprobar si los números de una columna son únicos.
if __name__ == '__main__':


    correct = [[1,2,3],
               [2,3,1],
               [3,1,2]]


    if numerosEnColumna(correct):
        print("No se repiten los num")
    else: 
        print("Se repiten los num")
    
 
    incorrect = [[1,2,3,4],
                 [2,3,1,3],
                 [3,1,2,3],
                 [4,4,4,2]]

    if numerosEnColumna(incorrect):
        print("No se repiten los num")
    else: 
        print("Se repiten los num")


    incorrect2 = [[1,2,3,4],
                  [2,3,1,2],
                  [4,1,2,3],
                  [2,3,1,4]]

    if numerosEnColumna(incorrect2):
        print("No se repiten los num")
    else: 
        print("Se repiten los num")


    incorrect3 = [[1,2,3,4,5],
                  [2,3,1,5,6],
                  [4,5,2,1,3],
                  [3,4,5,2,1],
                  [5,6,4,3,2]]

    if numerosEnColumna(incorrect3):
        print("No se repiten los num")
    else: 
        print("Se repiten los num")


    incorrect4 = [['a','b','c'],
                  ['b','c','a'],
                  ['c','a','b']]

    if numerosEnColumna(incorrect4):
        print("No se repiten los num")
    else: 
        print("Se repiten los num")


    incorrect5 = [ [1, 1.5],
                   [1.5, 1]]

    if numerosEnColumna(incorrect5):
        print("No se repiten los num")
    else: 
        print("Se repiten los num")


    irregular = [[1,2,3],
                 [2,3,1]]

    if numerosEnColumna(irregular):
        print("No se repiten los num")
    else: 
        print("Se repiten los num")


    irregular2 = [[1,2,3],
                  [2,3,1],
                  [3,1]]

    if numerosEnColumna(irregular2):
        print("No se repiten los num")
    else: 
        print("Se repiten los num")
