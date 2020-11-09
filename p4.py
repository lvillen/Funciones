#Lambdas (o funciones anónimas)

from p2 import sumaTodos 

#Opción 1

doble = lambda x: x*2

print(sumaTodos(3, doble))

#Opción 2

print(sumaTodos(3, lambda x: x**3)) 

'''
La lambda es: 
función sumaTodos, que requiere dos parámetros: 
1. Un limitTo, es decir, un número para las veces que quiera hacer la iteración de la función.
2. f, es decir, una función que aquí hacemos de forma anónima tal que así: lambda x: x**3.
    Siendo la x sobre lo que se realizará esta función, y siendo x**3 x elevado a la tercera potencia.
'''