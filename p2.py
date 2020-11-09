def normal(x): #La x solo funciona en el ámbito de la función, luego la voy a modificar al usar la función. [EJEMPLO]
    return x

def cuadrado(x):
    return x * x

def sumaTodos(limitTo, f) #Función de primer nivel
    resultado = 0
    for i in range(limitTo+1):
        resultado += f(i)

    return resultado

if __name__ == '__main__':
    print(sumaTodos(100, normal))
    print(sumaTodos(3, cuadrado))