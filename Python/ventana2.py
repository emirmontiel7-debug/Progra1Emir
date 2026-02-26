import tkinter as tk 
from tkinter import messagebox

def opcion():
    if var.get()==1:
        messagebox.showinfo("Opcion", "Te gustan los tacos")
    elif var.get()==2:
        messagebox.showinfo("Opcion", "Te gustan las chanclas")
    elif var.get()==3:
        messagebox.showinfo("Opcion", "Te gustan las Milanesas")
    elif var.get()==4:
        messagebox.showinfo("Opcion", "Te gustan la Pizza")   
    else:
        messagebox.showinfo("Opcion","No seleccionaste nada") 

ventana=tk.Tk()
ventana.title("Una ventana")
ventana.geometry("300x400")

etiqueta=tk.Label(ventana,text="Uso del radio botton")#label es la etiqueta
etiqueta.pack(pady=20)

var=tk.IntVar()#guargar un numero en un variable
rad1=tk.Radiobutton(ventana, text="Tacos",variable=var,value=1)
rad1.pack()
rad2=tk.Radiobutton(ventana, text=" Chanclas",variable=var,value=2)
rad2.pack()
rad3=tk.Radiobutton(ventana, text="Milanesa",variable=var,value=3)
rad3.pack()
rad4=tk.Radiobutton(ventana, text="Pizza",variable=var,value=4)
rad4.pack()

boton1=tk.Button(ventana,text="Verificar",command=opcion)
boton1.pack(pady=30)

ventana.mainloop()