##Ahora definimos la función para saber que los numeros no sean diferentes a la longitud del cuadrado, es decir que vayan des del 1 hasta la longitud máxima del cuadrado.

def numeroEnRango(sudoku):
    for lista in sudoku:
        for numero in lista:
            if isinstance(numero, str) or numero not in range(1,len(sudoku)+1):#tenemos que poner que la longitud sea +1 ya que el range coge des de (a, z-1) si hacemos (1,4) cogería hasta 1-3.
                return False
    return True


if __name__ == "__main__":
#Aqui exponemos los casos tests para comprobar que la función es correcta

    correct = [[1,2,3],
            [2,3,1],
            [3,1,2]]

    if numeroEnRango(correct):
        print("Está en Rango")
    else: 
        print("No Está en Rango")


    incorrect = [[1,2,3,4],
                [2,3,1,3],
                [3,1,2,3],
                [4,4,4,2]]

    if numeroEnRango(incorrect):
        print("Está en Rango")
    else: 
        print("No Está en Rango")


    incorrect2 = [[1,2,3,4],
                [2,3,1,2],
                [4,1,2,3],
                [2,3,1,4]]

    if numeroEnRango(incorrect2):
        print("Está en Rango")
    else: 
        print("No Está en Rango")


    incorrect3 = [[1,2,3,4,5],
                [2,3,1,5,6],
                [4,5,2,1,3],
                [3,4,5,2,1],
                [5,6,4,3,2]]

    if numeroEnRango(incorrect3):
        print("Está en Rango")
    else: 
        print("No Está en Rango")


    incorrect4 = [['a','b','c'],
                ['b','c','a'],
                ['c','a','b']]

    if numeroEnRango(incorrect4):
        print("Está en Rango")
    else: 
        print("No Está en Rango")


    incorrect5 = [ [1, 1.5],
                [1.5, 1]]

    if numeroEnRango(incorrect5):
        print("Está en Rango")
    else: 
        print("No Está en Rango")

    irregular = [[1,2,3],
                [2,3,1]]

    if numeroEnRango(irregular):
        print("Está en Rango")
    else: 
        print("No Está en Rango")


    irregular2 = [[1,2,3],
                [2,3,1],
                [3,1]]

    if numeroEnRango(irregular2):
        print("Está en Rango")
    else: 
        print("No Está en Rango")