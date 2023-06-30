#using parameters

def greet(name):
    #global name
    
    return f'hello {name} welcome'

greeting = greet('camilo')

print(greeting)

#suma

def sumar(a, b):
    return a + b
suma = sumar(10, 50)

print('the result:', suma)

#resta

def restar(a=None, b=None):
    if a == None or b == None:
        print('error')
        return
    return a - b
resta = restar(b = 10, a = 20)
print('the result:', resta)