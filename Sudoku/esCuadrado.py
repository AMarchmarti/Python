##En este apartado del sudoku definiremos la función para saber si el sudoku es cuadrado, eso significa que tenga el mismo numero de filas como columnas n * n

#Definimos la función esCuadrado
def esCuadrado(sudoku):
    for lista in sudoku:
        if len(lista) != len(sudoku): #Usamos la negación para que no haga más reiteraciones de la cuenta, es decir en el momento que encuentre alguna que no sea igual
            return False #se pare el programa y no siga ejecutando hasta terminar toda la estructura.
    return True

if __name__ == "__main__":
#Ahora expondremos nuestros casos test para comprobar que esta función es válida:

    sudoku = [[1,2,3],
              [2,3,4],
              [1,2]]

    if esCuadrado(sudoku):
        print("Es Cuadrado Ok")
    else: 
        print("Es Cuadrado Fail")


    sudoku2 = [[1,2,3],
               [2,3,4],
               [1,2,3]]

    if esCuadrado(sudoku2):
        print("Es Cuadrado Ok")
    else: 
        print("Es Cuadrado Fail")


    sudoku3= [[1,2,3,4],
              ["a","b","c","d"],
              [3,"e",5,6],
              [4,5,6,3]]

    if esCuadrado(sudoku3):
        print("Es Cuadrado Ok")
    else: 
        print("Es Cuadrado Fail")


    sudoku4= [[1,2,3],
              [2,3,4]]

    if esCuadrado(sudoku4):
        print("Es Cuadrado Ok")
    else: 
        print("Es Cuadrado Fail")