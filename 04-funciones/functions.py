#function to greet
#using the global instruction and function return

def greet():
    global name
    name = 'juan'
    age = 23
    return 'hello', name, age 

date = greet()
greeting, name, age = greet()

print(date)
print(greeting)
print(name, age)