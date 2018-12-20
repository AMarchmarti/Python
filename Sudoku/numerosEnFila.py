##Esta vez vamos a hacer una función donde nos diga que los numeros en la misma fila no se repitan.

def numerosEnFila(sudoku):
    for lista in sudoku:
        for numero in lista:
                if lista.count(numero) > 1:#el count es una función de python que cuenta los numeros que hay, por tanto le decimos que si cuenta más de una vez un mismo número pare el programa.
                    return False              
    return True

#Casos Tests: comprobar si los números de una fila son únicos.
if __name__ == '__main__':


    correct = [[1,2,3],
               [2,3,1],
               [3,1,2]]


    if numerosEnFila(correct):
        print("No se repiten los num")
    else: 
        print("Se repiten los num")
    
    
    incorrect = [[1,2,3,4],
                 [2,3,1,3],
                 [3,1,2,3],
                 [4,4,4,2]]

    if numerosEnFila(incorrect):
        print("No se repiten los num")
    else: 
        print("Se repiten los num")

    
    incorrect2 = [[1,2,3,4],
                  [2,3,1,2],
                  [4,1,2,3],
                  [2,3,1,4]]

    if numerosEnFila(incorrect2):
        print("No se repiten los num")
    else: 
        print("Se repiten los num")


    incorrect3 = [[1,2,3,4,5],
                  [2,3,1,5,6],
                  [4,5,2,1,3],
                  [3,4,5,2,1],
                  [5,6,4,3,2]]

    if numerosEnFila(incorrect3):
        print("No se repiten los num")
    else: 
        print("Se repiten los num")


    incorrect4 = [['a','b','c'],
                  ['b','c','a'],
                  ['c','a','b']]

    if numerosEnFila(incorrect4):
        print("No se repiten los num")
    else: 
        print("Se repiten los num")


    incorrect5 = [ [1, 1.5],
                   [1.5, 1]]

    if numerosEnFila(incorrect5):
        print("No se repiten los num")
    else: 
        print("Se repiten los num")


    irregular = [[1,2,3],
                 [2,3,1]]

    if numerosEnFila(irregular):
        print("No se repiten los num")
    else: 
        print("Se repiten los num")


    irregular2 = [[1,2,3],
                  [2,3,1],
                  [3,1]]

    if numerosEnFila(irregular2):
        print("No se repiten los num")
    else: 
        print("Se repiten los num")