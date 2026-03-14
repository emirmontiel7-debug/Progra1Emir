#1
class Persona():
    def __init__(self,idPersona,nombre,email):
        self.idPersona=idPersona
        self.nombre=nombre
        self.email=email

    def login(self):
        print (f"Sesion iniciada {self.nombre}")
    
    def actualizarPerfil(self):
        print("Tu perfil se actualizo")

class Cliente(Persona):
    def __init__(self, idPersona, nombre, email,puntosFidelidad,historialPedidos):
        super().__init__(idPersona, nombre, email)
        self.puntosFidelidad=puntosFidelidad
        self.historialPedidos=[]

    def realizarPedido(self,pedido):
        self.historialPedidos.append(pedido)
        print("se Registro el pedido correctamente")
    
    def consultarHistorial(self):
        print(f"{self.historialPedidos}")

    def canjearPuntos(self):
        print("Puntos disponibles para canje: " + str(self.puntosFidelidad))

class Empleado(Persona):
    def __init__(self, idPersona, nombre, email,idEmpleado,rol):
        super().__init__(idPersona, nombre, email)
        self.idEmpleado=idEmpleado
        self.rol=rol

    def actualizarInventario(self,inventario,ingrediente,cantidad):
        inventario.ingredientes[ingrediente]=cantidad

    def cambiarEstadoPedido(self,pedido,nuevoEstado):
        pedido.estado=nuevoEstado
#2
class ProductoBase():
    def __init__(self,idProducto,nombre,precioBase):
        self.idProducto=idProducto
        self.nombre=nombre
        self.precioBase=precioBase
    
class Bebida(ProductoBase):
    def __init__(self, idProducto, nombre, precioBase,tamaño,temperatura):
        super().__init__(idProducto, nombre, precioBase)
        self.tamaño=tamaño
        self.temperatura=temperatura
        self.modificadores=[]

    def agregarExtra(self,extra):
        self.modificadores.append(extra)

    def calcularPrecioFinal(self):
        return self.precioBase
    
class Postre(ProductoBase):
    def __init__(self, idProducto, nombre, precioBase,esVegano,sinGluten):
        super().__init__(idProducto, nombre, precioBase)
        self.esVegano=esVegano
        self.sinGluten=sinGluten
#3
class Pedido():
    def __init__(self,idPedido):
        self.idPedido=idPedido
        self.productos=[]
        self.estado="pendiente"
        self.total=0
    
    def calcularTotal(self):
        suma=0
        for p in self.productos:
            suma=suma+p.precioBase
        self.total=suma
        return self.total
    
    def validarStock():
        return True
    
class Inventario():
    def __init__(self):
        self.ingredientes=[]

    def reducirStock(self,ingrediente,cantidad):
        if ingrediente in self.ingredientes:
            self.ingredientes[ingrediente]-=cantidad

    def noticarFaltante(self):
        print("bajo stock")


    