# Importar Bibliotecas
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import sqlite3

# INTERFAZ GRAFICA
registro = Tk()
registro.title("Registro de clientes - Base de Datos")
registro.geometry("700x530")
registro.resizable(0, 0)
registro.config(bg='LightSteelBlue1')

#VARIABLES
id = StringVar()
nombre = StringVar()
info_ad = StringVar()
monto = StringVar()

def base_de_datos():
	conexion = sqlite3.connect("base_registro")
	cursor = conexion.cursor()

	try:
		cursor.execute('''
			CREATE TABLE cliente (
			ID INTEGER PRIMARY KEY AUTOINCREMENT,
			NOMBRE VARCHAR(50) NOT NULL,
			INFORMACION VARCHAR(50) NOT NULL,
			MONTO INT NOT NULL)
			''')
		messagebox.showinfo("CONEXION", "Base de Datos creada exitosamente")
	except:
		messagebox.showinfo("CONEXION", "Conexión exitosa con la base de datos")

def eliminar_base():
	conexion = sqlite3.connect("base_registro")
	cursor = conexion.cursor()
	if messagebox.askyesno(message="¿Los datos se perderan definitivamente, Desea continuar?", title="¡ADVERTENCIA!"):
		cursor.execute("DROP TABLE cliente")
	else:
		pass
	limpiar_campos()
	mostrar()

def limpiar_campos():
	id.set("")
	nombre.set("")
	info_ad.set("")
	monto.set("")

def crear():
	conexion = sqlite3.connect("base_registro")
	cursor = conexion.cursor()
	try:
		datos = nombre.get(), info_ad.get(), monto.get()
		cursor.execute("INSERT INTO cliente VALUES(NULL,?,?,?)", datos)
		conexion.commit()
	except:
		messagebox.showwarning("Error", " Crear la base de datos ")
		pass
	limpiar_campos()
	mostrar()

def mostrar():
	conexion = sqlite3.connect("base_registro")
	cursor = conexion.cursor()
	registros = tree.get_children()
	for elemento in registros:
		tree.delete(elemento)

	try:
		cursor.execute("SELECT * FROM cliente")
		for row in cursor:
			tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3]))
	except:
		pass

# CREAMOS LA TABLA
tree = ttk.Treeview(height=15, columns=('#0', '#1', '#2'))
tree.place(x=30, y=150)
tree.column('#0', width=100)
tree.heading('#0', text="ID", anchor=CENTER)
tree.heading('#1', text="Nombre del cliente", anchor=CENTER)
tree.heading('#2', text="Información adicional", anchor=CENTER)
tree.column('#3', width=120)
tree.heading('#3', text="Monto (S/.)", anchor=CENTER)

def seleccionar(event):
	item=tree.identify('item', event.x, event.y)
	id.set(tree.item(item, "text"))
	nombre.set(tree.item(item, "values")[0])
	info_ad.set(tree.item(item, "values")[1])
	monto.set(tree.item(item, "values")[2])

tree.bind("<Double-1>", seleccionar)

def actualizar():
	conexion = sqlite3.connect("base_registro")
	cursor = conexion.cursor()
	try:
		datos = nombre.get(), info_ad.get(), monto.get()
		cursor.execute("UPDATE cliente SET NOMBRE=?, INFORMACION=?, MONTO=? WHERE ID="+id.get(), datos)
		conexion.commit()
	except:
		messagebox.showwarning("Advertencia", "Seleccione el registro que desea modificar")
		pass
	limpiar_campos()
	mostrar()

def borrar():
	conexion = sqlite3.connect("base_registro")
	cursor = conexion.cursor()
	try:
		if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="Advertencia"):
			cursor.execute("DELETE FROM cliente WHERE ID="+id.get())
			conexion.commit()
	except:
		messagebox.showwarning("Advertencia", "Seleccione el registro que desea eliminar")
		pass
	limpiar_campos()
	mostrar()

# CREAMOS EL LA BARRA DE MENU
menubar = Menu(registro)
menubasedat = Menu(menubar, tearoff=0)
menubasedat.add_command(label="Crear Base de Datos", command=base_de_datos)
menubasedat.add_command(label="Eliminar Base de Datos", command=eliminar_base)
menubar.add_cascade(label="Barra de menú", menu=menubasedat)

# CREAMOS LAS ETIQUETAS Y CAJAS DE TEXTO
e1 = Entry(registro, textvariable=id)

l2 = Label(registro, text="Nombres y Apellidos: ", font=('Arial', 12, 'bold'), bg='LightSteelBlue2')
l2.place(x=50, y=10)
e2 = Entry(registro, textvariable=nombre, width=60)
e2.place(x=250, y=10)

l3 = Label(registro, text="Información adicional: ", font=('Arial', 12, 'bold'), bg='LightSteelBlue2')
l3.place(x=50, y=40)
e3 = Entry(registro, textvariable=info_ad, width=60)
e3.place(x=250, y=40)

l4 = Label(registro, text="Monto (S/.): ", font=('Arial', 12, 'bold'), bg='LightSteelBlue2')
l4.place(x=50, y=70)
e4 = Entry(registro, textvariable=monto, width=15)
e4.place(x=250, y=70)

# CREAMOS LOS BOTONES
b1 = Button(registro, text="Insertar Registro", command=crear)
b1.place(x=50, y=100)
b2 = Button(registro, text="Modificar Registro", command=actualizar)
b2.place(x=160, y=100)
b3 = Button(registro, text="Mostrar Lista", command=mostrar)
b3.place(x=280, y=100)
b4 = Button(registro, text="Limpiar casilleros", command=limpiar_campos)
b4.place(x=375, y=100)
b5 = Button(registro, text="Eliminar Registro", command=borrar)
b5.place(x=500, y=100)

registro.config(menu=menubar)
