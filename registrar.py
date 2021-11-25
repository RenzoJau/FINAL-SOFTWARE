#EN ESTA PARTE SI GENERA LA VENTANA, SOLO QUE SE AÑADE NI GENERA EL NOMBRE DEL ARCHIVO DE GUARDAR, NI DE LAS DEMAS ENTRIES, APARECE COMO nombre1 is not defined.
from tkinter import *
from tkinter import Tk, Label, Button, Entry, Frame, END, messagebox
import pandas as pd
import openpyxl

class Registro2 (Tk) :
	def __init__(self):
		super().__init__()
		self.config(bg='RoyalBlue4')
		self.geometry('398x550')
		self.resizable(0, 0)
		self.title('Guardar registro de datos')

		frame1 = Frame(self, bg='RoyalBlue4', padx=10)
		frame1.grid(column=0, row=0, sticky='W')
		frame2 = Frame(self, bg='DodgerBLue3', padx=22)
		frame2.grid(column=0, row=1, sticky='nsew')

		archivo = Label(frame1, text='Ingrese nombre del archivo', width=20, bg='RoyalBlue4',
							 font=('Arial', 12, 'bold'), fg='white')
		archivo.grid(column=0, row=0, pady=15, padx=20)

		nombre_archivo = Entry(frame1, width=30, font=('Arial', 13), highlightbackground="midnight blue",
									highlightthickness=4)
		nombre_archivo.grid(column=0, row=1, pady=15, padx=40)

		guardar = Button(frame1, width=15, font=('Arial', 14, 'bold'), text='Guardar', bg='DarkOrange1', bd=5,
							  command=self.guardar_datos)
		guardar.grid(column=0, row=2, pady=15, padx=20)

		cliente = Label(frame2, text='Ingrese información del cliente', width=30, bg='DodgerBLue3',
							 font=('Arial', 12, 'bold'), fg='white')
		cliente.grid(columnspan=2, row=0, pady=15, padx=20)

		self.nombre = Label(frame2, text='NOMBRE: ', width=10).grid(column=0, row=1, pady=20, padx=25)
		ingresa_nombre = Entry(frame2, width=25, font=('Arial', 13))
		ingresa_nombre.grid(column=1, row=1)

		self.apellido = Label(frame2, text='APELLIDO: ', width=10).grid(column=0, row=2, pady=10, padx=25)
		ingresa_apellido = Entry(frame2, width=25, font=('Arial', 13))
		ingresa_apellido.grid(column=1, row=2)

		self.dni = Label(frame2, text='DNI: ', width=10).grid(column=0, row=3, pady=10, padx=25)
		ingresa_dni = Entry(frame2, width=25, font=('Arial', 13))
		ingresa_dni.grid(column=1, row=3)

		self.celular = Label(frame2, text='CELULAR: ', width=10).grid(column=0, row=4, pady=10, padx=25)
		ingresa_celular = Entry(frame2, width=25, font=('Arial', 13))
		ingresa_celular.grid(column=1, row=4)

		self.monto = Label(frame2, text='MONTO: ', width=10).grid(column=0, row=5, pady=10, padx=25)
		ingresa_monto = Entry(frame2, width=25, font=('Arial', 13))
		ingresa_monto.grid(column=1, row=5)

		agregar = Button(frame2, width=15, font=('Arial', 14, 'bold'), text='Agregar', bg='DarkOrange1', bd=5,
							  command=self.agregar_datos)
		agregar.grid(columnspan=2, row=6, pady=15, padx=20)

		nombre1, apellido1, dni1,celular1, monto1 = [],[],[],[],[]

	def agregar_datos(self):
		global nombre1, apellido1, dni1, scelular1, monto1
		nombre1.append(self.ingresa_nombre.get())
		apellido1.append(self.ingresa_apellido.get())
		dni1.append(self.ingresa_dni.get())
		celular1.append(self.ingresa_celular.get())
		monto1.append(self.ingresa_monto.get())

		self.ingresa_nombre.delete(0, END)
		self.ingresa_apellido.delete(0, END)
		self.ingresa_dni.delete(0, END)
		self.ingresa_celular.delete(0, END)
		self.ingresa_monto.delete(0, END)

	def guardar_datos(self):
		global nombre1, apellido1, dni1, celular1, monto1
		datos = {'NOMBRE': nombre1, 'APELLIDO': apellido1, 'DNI': dni1, 'CELULAR': celular1,
				 'MONTO': monto1}
		nom_excel = str(self.nombre_archivo.get() + ".xlsx")
		df = pd.DataFrame(datos, columns=['NOMBRE', 'APELLIDO', 'DNI', 'CELULAR', 'MONTO'])
		df.to_excel(nom_excel)
		self.nombre_archivo.delete(0, END)
