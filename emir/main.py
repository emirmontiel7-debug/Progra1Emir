from humanidad import *

humano1=Humano("Diana", 17, "Femenino")
print(humano1.nombre)
print(humano1.edad)
print(humano1.genero)
humano1.caract()
humano1.saludo()

prog1=Programador("Jose",20,"masculino")
print(prog1.nombre)
print(prog1.edad)
print(prog1.genero)
prog1.caract()
prog1.saludo()
prog1.saludo2()

ing=Ingenierio("Ramira", 24, "masculino", "literatura")
print(ing.nombre)
print(ing.edad)
print(ing.genero)
ing.caract()
ing.saludo()
ing.saludo3()