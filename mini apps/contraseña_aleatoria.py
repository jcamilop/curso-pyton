
import random

def c_aleatoria():

    MAYUSCULAS = ['A','B','C','D','E','F','G','H','I','J']
    minusculas = ['a','b','c','d','e','f','g','h','i','j']
    numeros = [1,2,3,4,5,6,7,8,9,10]
    simbolos = ['#','$','@','!','%']

    caracteres = MAYUSCULAS + minusculas + numeros + simbolos
    contraseña = []

    for i in range(15):
        caracteres_aleatorios = random.choice(caracteres)
        contraseña.append(caracteres_aleatorios)
        
    contraseña = "".join(contraseña)
    return contraseña

def main():
    contraseña = c_aleatoria()
    print(contraseña)
    
if __name__ == '__main__':
    main()
    