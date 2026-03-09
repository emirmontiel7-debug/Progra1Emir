import csv
import os
class Usuario():
    lista=[]
    ruta_csv=r"C:/Users/DELL/Desktop/dan/Python_SegundosemestreBUAP-main/fron_end/personas.csv"
    def __init__ (self, name,age,food):
        self.nombre=name
        self.edad=age
        self.comida=food
        if self not in Usuario.lista:
            Usuario.lista.append(self)

    def mostrar_datos(self):
        return f"El usuario {self.nombre} tiene {self.edad} años y le gusta los {self.comida}"

    @classmethod #metodo de clase
    def mostrar_lista(cls):
        for u in Usuario.lista:
            print (u.mostrar_datos())

    @classmethod
    def guardar_archivo(cls):
        campos=["nombre", "edad","comida"]#nombres de la columna de la tabla

        #crear el directorio
        directorio= os.path.dirname(cls.ruta_csv)
        if not os.path.exists(directorio):
            try:
                os.makedirs(directorio)
                print(f"directorio creado {directorio}")
            except Exception as e:
                print(f"error al crear directorio: {e}")
                return False
            
        #guardar el archivo
        with open(cls.ruta_csv, "w", newline='',encoding="utf-8") as f:
            escritor=csv.DictWriter(f, fieldnames=campos, delimiter=',')
            escritor.writeheader()
            for u in cls.lista:
                escritor.writerow({"nombre":u.nombre,"edad":u.edad,"comida":u.comida})