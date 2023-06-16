n = int(input("ingrese un numero estero, "))

if n != 0:
   if n > 0:
        if n % 2 == 0:
            print(f'el numero {n} es par postitivo')
        else:
            print(f'el numero {n} es impar positivo')
   else:
       if n % 2 == 0:
           print(f'el numero {n} es par negativo')
       else:
           print(f'el numero {n} es impar negativo')
else:
    print(f'el numero {n} es neutro')