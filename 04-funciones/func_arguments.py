def sumar(*args, **kwargs):
    suma = 0
    for n in args:
        suma += n
    return suma, kwargs
suma_total, datos = sumar(10, 35,name = 'juan', age = 23)
print('the resul:', suma_total)
print(datos)