
def n_primo(numero): 
   contador = 0
   
   for i in range(1, numero+1):
    if i == 1 or i == numero:
        continue
    
    #divicion con los numero hasta llegar al numero ingresado
    
    if numero % i == 0:
            contador += 1    
    
    if contador == 0:
        return True
    else:
        return False

def main():
    numero = int(input('ingrese el numero: '))
    
    if n_primo(numero):
        print(f'el numero {numero} es primo')
    else:
        print(f'el numero {numero} no es primo')
        
if __name__ == '__main__':
    main()
    