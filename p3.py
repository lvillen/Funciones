def maxi(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for ix in range(1, len(l)):
        if l[ix] > m:
            m = l[ix]
    return m

def mini(*l):
    if len(l) == 0:
        return 0
    m = l[0]
    for ix in range(1, len(l)):
        if l[ix] < m:
            m = l[ix]
    return m    

def media(*l):
    if len(l) == 0:
        return 0
    suma = 0
    for valor in l:
        suma += valor
    return suma / len (l)

funciones = {
    'max' : maxi,
    'min' : mini,
    'med' : media
}

def returnF(nombre):
    nombre = nombre.lower()
    if nombre in funciones.keys():#me devuelve como iterables las keys.
        return funciones[nombre]
    return None

'''
Si quisiéramos ejecutar esta última función, tendríamos que hacerlo así:
returnF('max')(1, 3, -1, 15, 9)
La primera parte, returnF('max') llama a la función, la segunda parte de la línea nos da los parámetros de la función a la que estamos invocando.
'''
