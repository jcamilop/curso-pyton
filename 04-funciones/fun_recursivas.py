

def factorial(n):
    print('valor inicial:', n)
    if n > 1:
        n = n * factorial(n - 1)
    print('valor final:', n)
    return n

n = int(input('ingrese un numero: '))

F = factorial(n)
print(f'el factorial de {n} es: ', F)