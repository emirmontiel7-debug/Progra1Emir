class Persona:
    def __init__(self, id_persona, nombre, email, telefono):
        self.id_persona=id_persona
        self.nombre=nombre
        self.email=email
        self.telefono=telefono

class Usuario(Persona):
    def __init__(self, id_persona, nombre, email, telefono, puntosFidelidad):
        super().__init__(id_persona, nombre, email, telefono)
        self.puntosFidelidad=puntosFidelidad
        self.historialReservas=[]

class Empleado(Persona):
    def __init__(self, id_empleado, nombre, email, telefono, rol, horario):
        super().__init__(id_empleado, nombre, email, telefono)
        self.id_empleado=id_empleado
        self.rol=rol
        self.horario=horario
    
class Espacio:
    def __init__(self, idEspacio, nombre, ubicacion):
        self.idEspacio=idEspacio
        self.nombre=nombre
        self.ubicacion=ubicacion

class Sala(Espacio):
    def __init__(self, idEspacio, nombre, ubicacion, tipo, capacidadTotal):
        super().__init__(idEspacio, nombre, ubicacion)
        self.tipo=tipo
        self.capacidadTotal=capacidadTotal

class Pelicula:
    def __init__(self, titulo, duracion, clasificacion, genero):
        self.titulo=titulo
        self.duracion=duracion
        self.clasificacion=clasificacion
        self.genero=genero

    def mostrar_detalle(self):
        return f"{self.titulo} ({self.duracion} min) - Género: {self.genero}"

class Funcion:
    def __init__(self, pelicula, sala, horarioInicio, precioBase):
        self.pelicula=pelicula 
        self.sala=sala
        self.horarioInicio=horarioInicio
        self.precioBase=precioBase

class Reserva:
    def __init__(self, idReserva, usuario, funcion, asientos, montoTotal):
        self.idReserva=idReserva
        self.usuario=usuario
        self.funcion=funcion
        self.asientos=asientos
        self.montoTotal=montoTotal