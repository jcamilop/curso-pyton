print('tiempo en segundo horas y minutos')

Tsegundos = int(input('ingresar los segundos: '))

horas = 3600
minutos = 60

h = Tsegundos // horas
Tsegundos = Tsegundos % horas
m = Tsegundos // minutos
s = Tsegundos % minutos

print('='*25)
print('----conversion----')
print('horas: ',h)
print('minutos: ',m)
print('segundos: ',s)
print('='*25)
