import tkinter as tk
from tkinter import messagebox

def ventanas():
    if var2.get()==1:
        messagebox.showinfo("Vnetana de Informacion", "Aca puedes escribir info al usuario")
    elif var2.get()==2:
        messagebox.showwarning("ventana de advertencia", "Esta es una emergencia")
    elif var2.get()==3:
        messagebox.showerror("ventana de error", "Has comeido un error")
    elif var2.get()==4:
        respuesta=messagebox.askyesno("ventana de opcion","Te gusta esta clase")
        if respuesta:
            messagebox.showinfo("ventana de respuesta","mas te vale")
        else:
            messagebox.showinfo("Ventana de respuesta", "por eso vas a repobrar")
    elif var2.get()==5:
        respuesta=messagebox.askokcancel("ventana de opcion","Das tu alma a estas clase?")
        if respuesta:
            messagebox.showinfo("ventana de opcion","por eso vas a sacar 10")
        else:
            messagebox.showinfo("ventana de respuestas","Por eso repruebas")
    else:
        messagebox.showinfo("ventana de respuesta","No elegiste ninga respuesta")        


ventana=tk.Tk()
ventana.title("Uso de diferentes messagebox")
ventana.geometry("400x600")
ventana.config(bg="beige")

etiqueta=tk.Label(ventana,text="hola")
etiqueta.pack(pady=10)

var2=tk.IntVar()
mes1=tk.Radiobutton(ventana,text="Mostrar informacion",variable=var2,value=1)
mes1.pack(pady=20)
mes2=tk.Radiobutton(ventana,text="Adevertencia",variable=var2,value=2)
mes2.pack(pady=20)
mes3=tk.Radiobutton(ventana,text="Error",variable=var2,value=3)
mes3.pack(pady=20)
mes4=tk.Radiobutton(ventana,text="Pregunta si o no",variable=var2,value=4)
mes4.pack(pady=20)
mes5=tk.Radiobutton(ventana,text="Preguntar aceptar o cancelar",variable=var2,value=5)
mes5.pack(pady=20)
boton1=tk.Button(ventana, text="Sacar una ventana", command=ventanas)
boton1.pack(pady=20)


ventana.mainloop()