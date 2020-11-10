def retrocontador(e):
    prin("{},".format(e),end="")

    if e > 0:
        retrocontador(e-1)

retrocontador(10)

def sumatorio(n):
    if n > 0 #Mejor > 0 que != 0 porque si utilizamos un número negativo, se caerá el programa.
        return n + sumatorio(n-1)
    else:
        return 0

sumatorio(4)

#Ejemplos de recursividad.