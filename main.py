from uml2 import *

inventario=Inventario()#crear clientes y empleados
emple=Empleado(123,"juan","juan@gmail.com","JUAAN123","gerente")
cliente1=Cliente(10, "Sofia", "sofia@mail.com",0,2)
#tomar orden
print("usted ah ordenado un cafe")
cafe=Bebida(100,"vainilla",30,"mediano","caliente")
orden1=Pedido(12)
orden1.productos.append(cafe)
#hacer el proceso
cliente1.login()
print(f"estado incial: {orden1.estado}")
#cambiar el estado a preparando
emple.cambiarEstadoPedido(orden1,"preparando")
print(f"pedido: {orden1.estado}")
#entregado
emple.cambiarEstadoPedido(orden1,"entregado")
print(f"pedido: {orden1.estado}")