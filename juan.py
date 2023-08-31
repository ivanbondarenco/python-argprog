#Creo la clase Persona que tiene como párametro los 3 sueldos que recibe Juan.
class Persona:
    
    def __init__(self, sueldo1, sueldo2, sueldo3):
        self.sueldo1 = sueldo1
        self.sueldo2 = sueldo2
        self.sueldo3 = sueldo3
#Creo a la Persona juan       
juan = Persona(300,500,700)

#Creo funcion tipoSueldo para determinar el sueldo promedio de Juan e indicar que tipo de sueldo recibe
def tipoSueldo():
    promedio = juan.sueldo1 + juan.sueldo2 + juan.sueldo3 / 3 
    print('El sueldo promedio de de juan es de', round(promedio)) 
    if(promedio < 300):
        print("El sueldo es bajo")
    if(promedio > 300 and promedio < 900):
        print("El sueldo es medio")
    if(promedio > 900):
        print("El sueldo es mejor de lo normal")  
#Invoco la funcion tipoSueldo()  
tipoSueldo()
    