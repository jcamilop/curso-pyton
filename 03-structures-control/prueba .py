dias = ['Domingo', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sabado']
 
for dia in dias:
    if dia == "Lunes":
        continue
    elif dia == 'Viernes':
        break
    print(dia)