from modelos import *

print("--- REGISTRO MANUAL DE INVENTARIO (10 PELÍCULAS) ---")

p1 = Pelicula("Titanic", 194, "B", "Romance")
p2 = Pelicula("Shrek", 90, "AA", "Animación")
p3 = Pelicula("El Rey León", 88, "AA", "Animación")
p4 = Pelicula("Harry Potter 1", 152, "A", "Fantasía")
p5 = Pelicula("Avatar", 162, "B", "Ciencia Ficción")
p6 = Pelicula("Avengers: Endgame", 181, "B", "Acción")
p7 = Pelicula("Jurassic Park", 127, "B", "Aventura")
p8 = Pelicula("Coco", 105, "AA", "Animación")
p9 = Pelicula("Batman", 152, "B15", "Acción")
p10 = Pelicula("Rápido y Furioso", 106, "B", "Acción")

print(f"ID: 1  | {p1.mostrar_detalle()}")
print(f"ID: 2  | {p2.mostrar_detalle()}")
print(f"ID: 3  | {p3.mostrar_detalle()}")
print(f"ID: 4  | {p4.mostrar_detalle()}")
print(f"ID: 5  | {p5.mostrar_detalle()}")
print(f"ID: 6  | {p6.mostrar_detalle()}")
print(f"ID: 7  | {p7.mostrar_detalle()}")
print(f"ID: 8  | {p8.mostrar_detalle()}")
print(f"ID: 9  | {p9.mostrar_detalle()}")
print(f"ID: 10 | {p10.mostrar_detalle()}")

print("--- VALIDACIÓN DE DATOS FINALIZADA ---\n")

print("se inicia el proceso")
user = Usuario(88, "Carlos88", "c@mail.com", "555-1234", 150)
sala04 = Sala(4, "04", "Planta Baja", "IMAX", 100)
funcion1 = Funcion(p5, sala04, "20:00", 150)

print(f"Usuario: {user.nombre} (Puntos: {user.puntosFidelidad})")
print(f"Película: '{funcion1.pelicula.titulo}' | Sala: {funcion1.sala.nombre} ({funcion1.sala.tipo})")

print("Seleccione sus asientos: A1, A2, B5")
print("El asiento A2 ya está ocupado por la Reserva #882.")
print("seleccione asientos disponibles.")

print("\nSeleccione sus asientos: A1, A3, B5")
print("Asientos A1, A3, B5 bloqueados con exito.")
print("Monto base: $450.00")

print("Metodos indivisduales")
admin=Empleado(10, "Admin_Juan", "a@cine.com", "342423", "ADMIN", "Matutino")
print(f"Prueba gestionarFunciones: {admin.gestionarFunciones()}")
print(f"Prueba limpiarEspacio: {sala04.limpiarEspacio()}")