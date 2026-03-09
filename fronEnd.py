import tkinter as tk
from backen import *
from tkinter import messagebox

def ventana_principal():
    ventana=tk.Tk()
    ventana.title("Base de datos")
    ventana.geometry("500x400")

    etiqueta1= tk.Label(ventana, text="Nombre")
    etiqueta1.pack()
    entrada1=tk.Entry(ventana,width=40)
    entrada1.pack(pady=15)

    etiqueta2=tk.Label(ventana, text="Edad")
    etiqueta2.pack(pady=15)
    entrada2=tk.Entry(ventana, width=40)
    entrada2.pack()

    etiqueta3=tk.Label(ventana, text="Comida Favorita")
    etiqueta3.pack(pady=15)
    entrada3=tk.Entry(ventana, width=40)
    entrada3.pack(pady=15)

    def registrar():
        name=entrada1.get()
        age=entrada2.get()
        food=entrada3.get()
        newuser=Usuario(name,age,food)
        entrada1.delete(0,tk.END)
        entrada2.delete(0,tk.END)
        entrada3.delete(0,tk.END)
        messagebox.showinfo("Registro de ususario","Tu registro fue exitoso")


    boton1=tk.Button(ventana, text="Registrar", command=registrar)
    boton1.pack(pady=20)
    def mostrar():
        Usuario.mostrar_lista()

    boton2=tk.Button(ventana, text="Mostrar Lista", command=mostrar)
    boton2.pack(pady=20)

    def al_cerrar():
        print("guardando datos antes de salir...")
        Usuario.guardar_archivo()
        ventana.destroy()

    #configaracion de que pasa al cerror la ventana
    ventana.protocol("WM_DELETE_WINDOW", al_cerrar)


    ventana.mainloop()

ventana_principal()