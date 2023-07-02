def palindromo(p):
    p = p.replace(' ','')
    p = p.lower()

    p_invertida = p [::-1]
    
    if p == p_invertida:
        return True
    else:
        return False
    
def main():
    p= input('ingrese una palabra: ')
    
    es_palindromo = palindromo(p)
    
    if es_palindromo:
        print(f'la palabra {p} es palindromo')
    
    else:
        print(f'la palabra {p} no es palindromo')
    
    
if __name__ == '__main__':
    main()
    
    