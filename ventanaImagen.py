import tkinter as tk
from PIL import Image, ImageTk

def boton_clic():
    print("hiciste un clic")

# 1. Crear la ventana correctamente con paréntesis
ven1 = tk.Tk() 
ven1.title("Mi aplicación con Imagen")
ven1.geometry("800x600")

# Etiquetas (Labels)
etiqueta = tk.Label(ven1, text="Hola, Grupo de programación Básica!",
                    font=("Arial", 14, "bold"), fg="black", bg="yellow", padx=20, pady=10)
etiqueta.pack(pady=5)

eti2 = tk.Label(ven1, text="Me llamo Emir Montiel",
                font=("Arial", 14, "bold"), fg="black", bg="yellow", padx=20, pady=10)
eti2.pack(pady=5)

# Cargar la imagen
try:
    imagen = Image.open("homero.png") # Asegúrate de que el archivo esté en la misma carpeta
    imagen = imagen.resize((400, 200))
    
    # El comando correcto es PhotoImage (termina en 'e')
    imagen_tk = ImageTk.PhotoImage(imagen)
    
    # Creamos el label para la imagen
    label_imagen = tk.Label(ven1, image=imagen_tk)
    
    # IMPORTANTE: Guardar una referencia de la imagen para que Python no la borre de la memoria
    label_imagen.image = imagen_tk 
    
    label_imagen.pack(pady=20)
except FileNotFoundError:
    print("Error: No encontré el archivo 'homero.png'. Revisa que esté en la misma carpeta.")

# El bucle principal para que la ventana no se cierre
ven1.mainloop()