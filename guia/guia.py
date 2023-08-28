# función para el botón de registro
def registrar_producto():
    nombre = entry_nombre.get() 
    descripcion = entry_descripcion.get()
    stock = entry_stock.get()
    precio = entry_precio.get()
    
    mensaje = f "Producto rgistrado:\nNombre: {nombre}\nDescripción: {descripcion}\nStock: {stock}\nPrecio: {precio}&"
    messagebox.showinfo(&"Registro Exitoso&", mensaje)

import tkinter as tk
from tkinter import messagebox
# configuracion de la ventana
ventana = tk.Tk()
ventana.title(&"Registro de Producto&")
ventana.geometry(""400x300 &quot";   )
label_nombre = tk.Label(ventana, text=&"Nombre del Producto:&")
label_nombre.pack()
entry_nombre = tk.Entry(ventana)
entry_nombre.pack()
label_descripcion = tk.Label(ventana, text=&"Descripción del Producto:&")
label_descripcion.pack()
entry_descripcion = tk.Entry(ventana)
entry_descripcion.pack()
label_stock = tk.Label(ventana, text=&"Stock del Producto:&")
label_stock.pack()
entry_stock = tk.Entry(ventana)
entry_stock.pack()
label_precio = tk.Label(ventana, text=&"Precio del Producto:&")
label_precio.pack()
entry_precio = tk.Entry(ventana)
entry_precio.pack()
# boton de registro
boton_registrar = tk.Button(ventana, text=&"Registrar Producto&",
command=registrar_producto)
boton_registrar.pack()
# iniciar la ventana
ventana.mainloop()