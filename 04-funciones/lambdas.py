#se usa en expresiones cortas

sumar = lambda a,b: a+b
print(sumar(10, 20))

restar = lambda a,b: a-b
print(restar(100,20))

par = lambda n: n % 2 == 0
print(par(4))

inpar = lambda n: n % 2 != 0
print(inpar(5))

revertir = lambda cadena: cadena[::-1]
print(revertir('hola'))