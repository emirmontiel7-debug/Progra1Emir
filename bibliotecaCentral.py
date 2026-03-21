class Material():
    def __init__(self,idMaterial,titulo,añoPublicacion,disponible):
        self.idMaterial=idMaterial
        self.titulo=titulo
        self.añoPublicacion=añoPublicacion
        self.disponible=disponible

class Libro(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible,autor,isbn,genero):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)
        self.autor=autor
        self.isbn=isbn
        self.genero=genero
    
class Revista(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible, edicion, periodicidad):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)
        self.edicion = edicion
        self.periodicidad = periodicidad 
        
class MaterialDigital(Material):
    def __init__(self, idMaterial, titulo, añoPublicacion, disponible,tipoArchivo,urlDescarga,tamañoMB):
        super().__init__(idMaterial, titulo, añoPublicacion, disponible)
        self.tipoArchivo=tipoArchivo
        self.urlDescarga=urlDescarga
        self.tamañoMB=tamañoMB

class Persona:
    def __init__(self, nombre):
        self.nombre=nombre

class Usuario(Persona):
    def __init__(self, nombre,limitePrestamos):
        super().__init__(nombre)
        self.limitePrestamos=limitePrestamos
        self.listaActiva = None

class Bibliotecario(Persona):
   def gestionarPrestamo(self):
       print("preparando prestamo")
    
   def transferirMaterial(self):
       print("enviaodo a su destino:sucursal")

class Sucursal():
    def __init__(self,idSucursal,nombre,capacidad):
        self.idSucursal=idSucursal
        self.nombre=nombre
        self.capacidad=capacidad
        self.catalogoLocal=None

class Prestamo():
    def __init__(self,idPrestamo,fechaInicio,fechaDevolucion,usuario,material):
        self.idPrestamo=idPrestamo
        self.fechaInicio=fechaInicio
        self.fechaDevolucion=fechaDevolucion
        self.usuario=usuario
        self.material=material

class Penalizacion():
    def __init__(self,monto,motivo,pagada):
        self.monto=monto
        self.motivo=motivo
        self.pagada=pagada
    
    def calcularMulta(self):
        print("calculando multa")
    def bloquearUsuario(self):
        print("bloqueando")
    
class Catalogo:
    def buscarPorAutor(self, autor):
        print("buscando autor.")
        
    def buscarEnTodasSucursales(self, criterio):
        print("buscando en sucursales")