from bibliotecaCentral import *

sucursal1=Sucursal(1,"Sede1",12)
sucursal2=Sucursal(2,"sede2",13)

L1=Libro(101, "Cien Años de Soledad", 1967, True, "García Márquez", "978-01", "Realismo")
L2=Libro(102, "1984", 1949, True, "George Orwell", "978-02", "Distopía")
L3=Libro(103, "El Principito", 1943, True, "Saint-Exupéry", "978-03", "Infantil")
L4 = Libro(104, "Don Quijote", 1605, True, "Cervantes", "978-04", "Clásico")
L5 = Libro(105, "Rayuela", 1963, True, "Julio Cortázar", "978-05", "Novela")
L6 = Libro(106, "Fahrenheit 451", 1953, True, "Ray Bradbury", "978-06", "Ciencia Ficción")
L7 = Libro(107, "El Aleph", 1949, True, "Jorge Luis Borges", "978-07", "Cuento")
L8 = Libro(108, "Pedro Páramo", 1955, True, "Juan Rulfo", "978-08", "Realismo")
L9 = Libro(109, "La Tregua", 1960, True, "Mario Benedetti", "978-09", "Drama")
L10 = Libro(110, "Ensayo sobre la Ceguera", 1995, True, "Saramago", "978-10", "Filosófico")

R1 = Revista(201, "National Geographic", 2024, True, 120, "Mensual")
R2 = Revista(202, "Scientific American", 2024, True, 85, "Mensual")
R3 = Revista(203, "Time", 2024, True, 1050, "Semanal")
R4 = Revista(204, "Vogue", 2024, True, 300, "Mensual")
R5 = Revista(205, "Nature", 2024, True, 50, "Semanal")
R6 = Revista(206, "The Economist", 2024, True, 45, "Semanal")
R7 = Revista(207, "Muy Interesante", 2024, True, 210, "Mensual")
R8 = Revista(208, "Forbes", 2024, True, 98, "Mensual")
R9 = Revista(209, "Rolling Stone", 2024, True, 115, "Mensual")
R10 = Revista(210, "Cosmopolitan", 2024, True, 400, "Mensual")

U1 = Usuario("Ana García", 3)
U2 = Usuario("Beto Ortiz", 5)
U3 = Usuario("Carla Ruiz", 2)
U4 = Usuario("Diego Luna", 4)
U5 = Usuario("Elena Paz", 3)
U6 = Usuario("Fabio Sol", 6)
U7 = Usuario("Gaby Mar", 1)
U8 = Usuario("Hugo Rey", 5)
U9 = Usuario("Iris Luz", 2)
U10 = Usuario("Jair Noé", 4)

P1 = Prestamo(1, "2024-01-01", "2024-01-10", U1, L1)
P2 = Prestamo(2, "2024-01-02", "2024-01-11", U2, L2)
P3 = Prestamo(3, "2024-01-03", "2024-01-12", U3, R1)
P4 = Prestamo(4, "2024-01-04", "2024-01-13", U4, R2)
P5 = Prestamo(5, "2024-01-05", "2024-01-14", U5, L1)
P6 = Prestamo(6, "2024-01-06", "2024-01-15", U6, L2)
P7 = Prestamo(7, "2024-01-07", "2024-01-16", U7, L3)
P8 = Prestamo(8, "2024-01-08", "2024-01-17", U8, L4)
P9 = Prestamo(9, "2024-01-09", "2024-01-18", U9, R3)
P10 = Prestamo(10, "2024-01-10", "2024-01-19", U10, R3)


print("Sucursal:", sucursal1.nombre)
print("Préstamo 10 asignado a:", P1.usuario.nombre)

print("Sucursal:", sucursal2.nombre)
print("Préstamo 10 asignado a:", P2.usuario.nombre)

print("Sucursal:", sucursal2.nombre)
print("Préstamo 10 asignado a:", P3.usuario.nombre)

print("Sucursal:", sucursal1.nombre)
print("Préstamo 10 asignado a:", P4.usuario.nombre)

print("Sucursal:", sucursal1.nombre)
print("Préstamo 10 asignado a:", P5.usuario.nombre)

print("Sucursal:", sucursal2.nombre)
print("Préstamo 10 asignado a:", P6.usuario.nombre)

print("Sucursal:", sucursal1.nombre)
print("Préstamo 10 asignado a:", P7.usuario.nombre)

print("Sucursal:", sucursal1.nombre)
print("Préstamo 10 asignado a:", P8.usuario.nombre)

print("Sucursal:", sucursal1.nombre)
print("Préstamo 10 asignado a:", P9.usuario.nombre)

print("Sucursal:", sucursal2.nombre)
print("Préstamo 10 asignado a:", P10.usuario.nombre)

