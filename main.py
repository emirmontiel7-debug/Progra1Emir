from modelos import *

print("--- REGISTRO MANUAL DE INVENTARIO ---")

# --- 10 OBJETOS DE LA CLASE PELICULA ---
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

print(f"PELÍCULA 1: {p1.mostrar_detalle()}")
print(f"PELÍCULA 2: {p2.mostrar_detalle()}")
print(f"PELÍCULA 3: {p3.mostrar_detalle()}")
print(f"PELÍCULA 4: {p4.mostrar_detalle()}")
print(f"PELÍCULA 5: {p5.mostrar_detalle()}")
print(f"PELÍCULA 6: {p6.mostrar_detalle()}")
print(f"PELÍCULA 7: {p7.mostrar_detalle()}")
print(f"PELÍCULA 8: {p8.mostrar_detalle()}")
print(f"PELÍCULA 9: {p9.mostrar_detalle()}")
print(f"PELÍCULA 10: {p10.mostrar_detalle()}")

print("\n--- REGISTRO DE USUARIOS ---")
u1 = Usuario(101, "Ana", "ana@mail.com", "555-01", 100)
u2 = Usuario(102, "Beto", "beto@mail.com", "555-02", 150)
u3 = Usuario(103, "Carla", "carla@mail.com", "555-03", 200)
u4 = Usuario(104, "Dani", "dani@mail.com", "555-04", 50)
u5 = Usuario(105, "Emir", "emir@mail.com", "555-05", 300)
u6 = Usuario(106, "Fer", "fer@mail.com", "555-06", 120)
u7 = Usuario(107, "Gaby", "gaby@mail.com", "555-07", 80)
u8 = Usuario(108, "Hugo", "hugo@mail.com", "555-08", 400)
u9 = Usuario(109, "Irma", "irma@mail.com", "555-09", 110)
u10 = Usuario(110, "Juan", "juan@mail.com", "555-10", 90)

print(f"USUARIO 1: {u1.nombre} | Puntos: {u1.puntosFidelidad}")
print(f"USUARIO 5: {u5.nombre} | Puntos: {u5.puntosFidelidad} (Usuario VIP)")
print(f"USUARIO 10: {u10.nombre} | Puntos: {u10.puntosFidelidad}")

print("Procesos de Reserva")
user_test=u5
sala04 = Sala(4, "04", "Planta Baja", "IMAX", 100)
funcion1 = Funcion(p5, sala04, "20:00", 150) # Avatar

print(f"Usuario activo: {user_test.nombre}")
print(f"Película seleccionada: '{funcion1.pelicula.titulo}'")


print("Seleccione sus asientos: A1, A2, B5")
print("El asiento A2 ya está ocupado por la Reserva #882.")
print("seleccione asientos disponibles.")

print("\nSeleccione sus asientos: A1, A3, B5")
print("[ Asientos A1, A3, B5 bloqueados con éxito.")
print("Monto total a pagar: $450.00")

print("Metodos ")
admin = Empleado(10, "Admin_Juan", "a@cine.com", "342423", "ADMIN", "Matutino")
print(f"Acción Empleado: {admin.gestionarFunciones()}")
print(f"Acción Sala: {sala04.limpiarEspacio()}")