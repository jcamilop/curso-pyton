class Persona:
   
    def __init__(self, nombre, edad, ciudad):
            self.nombre = nombre 
            self.edad = edad
            self.ciudad = ciudad
        
    def dates(self):
            print('nombre:',self.nombre)
            print('edad:',self.edad)
            print('ciudad:',self.ciudad)