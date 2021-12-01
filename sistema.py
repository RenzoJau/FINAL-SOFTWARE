from tkinter import *
from tkinter import messagebox, filedialog, ttk, Tk, Button, Frame
import random
import time
import sqlite3

class SISTEMA_GESTION(Tk):
    def __init__(self):
        super().__init__()
        self.geometry('1270x690+0+0')
        self.resizable(0, 0)
        self.title('Sistema de Pedido del restaurante "La Chimbotana"')
        self.config(bg='lightgray')

        top_frame = Frame(self, bd=12, relief=RIDGE, bg='blue4')
        top_frame.pack(side=TOP)

        label_title = Label(top_frame, text='Restaurante "La Chimbotana" ', font=('arial', 30, 'bold'), fg='gold'
                            , bd=9, bg='blue4', width=51)
        label_title.grid(row=0, column=0)

        menu_frame = Frame(self, bd=8, relief=RIDGE, bg='SlateGray2')
        menu_frame.pack(side=LEFT)

        costo_frame = Frame(menu_frame, bd=6, relief=RIDGE, pady=15, bg='DodgerBlue4')
        costo_frame.pack(side=BOTTOM)

        entrada_frame = LabelFrame(menu_frame, text='Entradas', font=('arial', 16, 'bold'), bd=6, relief=RIDGE,
                                   fg='firebrick3')
        entrada_frame.pack(side=LEFT)

        fondo_frame = LabelFrame(menu_frame, text='Menú', font=('arial', 16, 'bold'), bd=6, relief=RIDGE,
                                 fg='firebrick3', pady=10)
        fondo_frame.pack(side=LEFT)

        bebida_frame = LabelFrame(menu_frame, text='Bebidas', font=('arial', 16, 'bold'), bd=6, relief=RIDGE,
                                  fg='firebrick3')
        bebida_frame.pack(side=LEFT)

        sistema_frame = Frame(self, bd=8, relief=RIDGE, pady=15)
        sistema_frame.pack(side=RIGHT)

        pedido_frame = LabelFrame(sistema_frame, text='PEDIDO', font=('arial', 19, 'bold'), bd=6, relief=RIDGE,
                                  fg='steel blue')
        pedido_frame.pack(side=BOTTOM)

        caja_frame = LabelFrame(sistema_frame, text='CAJA', font=('arial', 19, 'bold'), bd=6, relief=RIDGE,
                                fg='steel blue')
        caja_frame.pack(side=TOP)

        recibo_frame = Frame(sistema_frame, bd=4, relief=RIDGE)
        recibo_frame.pack()

        # Variables
        var1 = IntVar()
        var2 = IntVar()
        var3 = IntVar()
        var4 = IntVar()
        var5 = IntVar()
        var6 = IntVar()
        var7 = IntVar()
        var8 = IntVar()
        var9 = IntVar()
        var10 = IntVar()
        var11 = IntVar()
        var12 = IntVar()
        var13 = IntVar()
        var14 = IntVar()
        var15 = IntVar()
        var16 = IntVar()
        var17 = IntVar()
        var18 = IntVar()
        var19 = IntVar()
        var20 = IntVar()

        e_e1 = StringVar()
        e_e2 = StringVar()
        e_e3 = StringVar()
        e_e4 = StringVar()
        e_p1 = StringVar()
        e_p2 = StringVar()
        e_p3 = StringVar()
        e_p4 = StringVar()
        e_p5 = StringVar()
        e_p6 = StringVar()
        e_p7 = StringVar()
        e_p8 = StringVar()
        e_p9 = StringVar()
        e_p10 = StringVar()
        e_p11 = StringVar()
        e_b1 = StringVar()
        e_b2 = StringVar()
        e_b3 = StringVar()
        e_b4 = StringVar()
        e_b5 = StringVar()

        e_e1.set('0')
        e_e2.set('0')
        e_e3.set('0')
        e_e4.set('0')
        e_p1.set('0')
        e_p2.set('0')
        e_p3.set('0')
        e_p4.set('0')
        e_p5.set('0')
        e_p6.set('0')
        e_p7.set('0')
        e_p8.set('0')
        e_p9.set('0')
        e_p10.set('0')
        e_p11.set('0')
        e_b1.set('0')
        e_b2.set('0')
        e_b3.set('0')
        e_b4.set('0')
        e_b5.set('0')

        cevar = StringVar()
        cpvar = StringVar()
        cbvar = StringVar()
        stvar = StringVar()
        imvar = StringVar()
        ctvar = StringVar()

        # FUNCIONES DE PEDIDO
        def bt_total():
            global precio_Entrada, precio_Fondo, precio_Bebida, sub_total, impuesto
            if var1.get() != 0 or var2.get() != 0 or var3.get() != 0 or var4.get() != 0 or var5.get() != 0 or\
                    var6.get() != 0 or var7.get() != 0 or var8.get() != 0 or var9.get() != 0 or var10.get() != 0 or\
                    var11.get() != 0 or var12.get() != 0 or var13.get() != 0 or var14.get() != 0 or var15.get() != 0 \
                    or var16.get() != 0 or var17.get() != 0 or var18.get() != 0 or var19.get() != 0 or var20.get() != 0:

                item1 = int(e_e1.get())
                item2 = int(e_e2.get())
                item3 = int(e_e3.get())
                item4 = int(e_e4.get())

                item5 = int(e_p1.get())
                item6 = int(e_p2.get())
                item7 = int(e_p3.get())
                item8 = int(e_p4.get())
                item9 = int(e_p5.get())
                item10 = int(e_p6.get())
                item11 = int(e_p7.get())
                item12 = int(e_p8.get())
                item13 = int(e_p9.get())
                item14 = int(e_p10.get())
                item15 = int(e_p11.get())

                item16 = int(e_b1.get())
                item17 = int(e_b2.get())
                item18 = int(e_b3.get())
                item19 = int(e_b4.get())
                item20 = int(e_b5.get())

                precio_Entrada = (item1 * 5) + (item2 * 5) + (item3 * 5) + (item4 * 5)
                precio_Fondo = (item5 * 13) + (item6 * 13) + (item7 * 14) + (item8 * 14) + (item9 * 14) +\
                               (item10 * 14) + (item11 * 14) + (item12 * 14) + (item13 * 15) + (item14 * 15) +\
                               (item15 * 15)
                precio_Bebida = (item16 * 10) + (item17 * 10) + (item18 * 10) + (item19 * 8) + (item20 * 8)

                cevar.set('S/. ' + str("{:.2f}".format(precio_Entrada)))
                cpvar.set('S/. ' + str("{:.2f}".format(precio_Fondo)))
                cbvar.set('S/.' + str("{:.2f}".format(precio_Bebida)))

                sub_total = ((precio_Entrada + precio_Fondo + precio_Bebida)-0.18*(precio_Entrada + precio_Fondo +
                                                                                   precio_Bebida))
                stvar.set('S/. ' + str("{:.2f}".format(sub_total)))

                impuesto = ((precio_Entrada + precio_Fondo + precio_Bebida)*0.18)
                imvar.set('S/. ' + str("{:.2f}".format(impuesto)))

                costototal = sub_total + impuesto
                ctvar.set('S/. ' + str("{:.2f}".format(costototal)))

            else:
                messagebox.showerror('Error', 'No ha seleccionado ningún item')

        def registrar():
            global monto
            registro = Toplevel()
            registro.title("Registro de clientes - Base de Datos")
            registro.geometry("800x600")
            registro.resizable(0, 0)
            registro.config(bg='LightSteelBlue1')

            # VARIABLES
            id = StringVar()
            nombre = StringVar()
            dni = StringVar()
            direccion = StringVar()
            ncelular = StringVar()
            monto = StringVar()

            def base_de_datos():
                conexion = sqlite3.connect("base_registro")
                el_cursor = conexion.cursor()

                #AUTOINCREMENT
                try:
                    el_cursor.execute('''
                        CREATE TABLE Ventas (
                        ID integer PRIMARY KEY,
                        NOMBRE VARCHAR(50) NOT NULL,
                        DNI VARCHAR(50) NOT NULL,
                        DIRECCION VARCHAR(50) NOT NULL,
                        NCELULAR VARCHAR(50) NOT NULL,
                        MONTO INT NOT NULL)
                        ''')
                    messagebox.showinfo("CONEXION", "Base de Datos conectada exitosamente")
                except:
                    messagebox.showinfo("CONEXION", "Conexión exitosa con la base de datos")

            def eliminar_base():
                conexion = sqlite3.connect("base_registro")
                el_cursor = conexion.cursor()
                if messagebox.askyesno(message="¿Los datos se perderan definitivamente, Desea continuar?",
                                       title="¡ADVERTENCIA!"):
                    el_cursor.execute("DROP TABLE Ventas")
                else:
                    pass
                limpiar_campos()
                mostrar()

            def limpiar_campos():
                c_e1.delete(0,END)
                c_e2.delete(0, END)
                c_e3.delete(0, END)
                c_e4.delete(0, END)
                c_e5.delete(0, END)
                c_e6.delete(0, END)
                #c_e7.delete(0, END)

            def crear():
                conexion = sqlite3.connect("base_registro")
                el_cursor = conexion.cursor()
                try:
                    datos = nombre.get(), dni.get(), direccion.get(), ncelular.get(), monto.get()
                    el_cursor.execute("INSERT INTO Ventas VALUES(NULL,?,?,?,?,?)", datos)
                    conexion.commit()
                except:
                    messagebox.showwarning("Error", " Crear la base de datos ")
                    pass
                limpiar_campos()
                mostrar()

            def mostrar():
                conexion = sqlite3.connect("base_registro")
                el_cursor = conexion.cursor()
                registros = tree.get_children()
                for elemento in registros:
                    tree.delete(elemento)
                try:
                    el_cursor.execute("SELECT * FROM Ventas")
                    for row in el_cursor:
                        tree.insert("", 0, text=row[0], values=(row[1], row[2], row[3], row[4], row[5]))
                except:
                    pass

            # CREAMOS LA TABLA
            tree = ttk.Treeview(registro, height=14, columns=('#0', '#1', '#2', '#3', '#4'))
            tree.place(x=30, y=200)
            tree.column('#0', width=50)
            tree.heading('#0', text="ID", anchor=CENTER)
            tree.heading('#1', text="Nombre", anchor=CENTER)
            tree.heading('#2', text="DNI", anchor=CENTER)
            tree.column('#2', width=100)
            tree.heading('#3', text="Dirección", anchor=CENTER)
            tree.heading('#4', text="NCelular", anchor=CENTER)
            tree.column('#4', width=100)
            tree.heading('#5', text="Monto (S/.)", anchor=CENTER)
            tree.column('#5', width=100)

            def seleccionar(event):
                item = tree.identify('item', event.x, event.y)
                id.set(tree.item(item, "text"))
                nombre.set(tree.item(item, "values")[0])
                dni.set(tree.item(item, "values")[1])
                direccion.set(tree.item(item, "values")[2])
                ncelular.set(tree.item(item, "values")[3])
                monto.set(tree.item(item, "values")[4])

            tree.bind("<Double-1>", seleccionar)

            def actualizar():
                conexion = sqlite3.connect("base_registro")
                el_cursor = conexion.cursor()
                try:
                    datos = nombre.get(), dni.get(), direccion.get(), ncelular.get(), monto.get()
                    el_cursor.execute("UPDATE Ventas SET NOMBRE=?, DNI=?, DIRECCION=?, NCELULAR=?\
                                      , MONTO=? WHERE ID=" + id.get(), datos)
                    conexion.commit()
                except:
                    messagebox.showwarning("Advertencia", "Seleccione el registro que desea modificar")
                    pass
                limpiar_campos()
                mostrar()

            def borrar():
                conexion = sqlite3.connect("base_registro")
                el_cursor = conexion.cursor()
                try:
                    if messagebox.askyesno(message="¿Realmente desea eliminar el registro?", title="Advertencia"):
                        el_cursor.execute("DELETE FROM Ventas WHERE ID=" + id.get())
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
            c_e1 = Entry(registro, textvariable=id)
            c_e1.place()

            l2 = Label(registro, text="Nombres y Apellidos: ", font=('Arial', 12, 'bold'), bg='LightSteelBlue2')
            l2.place(x=50, y=10)
            c_e2 = Entry(registro, textvariable=nombre, width=60)
            c_e2.place(x=250, y=10)

            l3 = Label(registro, text="DNI: ", font=('Arial', 12, 'bold'), bg='LightSteelBlue2')
            l3.place(x=50, y=40)
            c_e3 = Entry(registro, textvariable=dni, width=30)
            c_e3.place(x=250, y=40)

            l4 = Label(registro, text="Dirección: ", font=('Arial', 12, 'bold'), bg='LightSteelBlue2')
            l4.place(x=50, y=70)
            c_e4 = Entry(registro, textvariable=direccion, width=60)
            c_e4.place(x=250, y=70)

            l5 = Label(registro, text="N. Celular: ", font=('Arial', 12, 'bold'), bg='LightSteelBlue2')
            l5.place(x=50, y=100)
            c_e5 = Entry(registro, textvariable=ncelular, width=30)
            c_e5.place(x=250, y=100)

            l6 = Label(registro, text="Monto (S/.): ", font=('Arial', 12, 'bold'), bg='LightSteelBlue2')
            l6.place(x=50, y=130)
            c_e6 = Entry(registro, textvariable=monto, width=15)
            c_e6.place(x=250, y=130)

            #l7 = Label(registro, text="Monto (S/.): ", font=('Arial', 12, 'bold'), bg='LightSteelBlue2')
            #l7.place(x=50, y=130)
            #c_e7 = Entry(registro, textvariable=monto_total, width=15, state='readonly')
            #c_e7.place(x=500, y=430)

            # CREAMOS LOS BOTONES
            b1 = Button(registro, text="Insertar Registro", command=crear)
            b1.place(x=50, y=160)
            b2 = Button(registro, text="Modificar Registro", command=actualizar)
            b2.place(x=160, y=160)
            b3 = Button(registro, text="Mostrar Lista", command=mostrar)
            b3.place(x=280, y=160)
            b4 = Button(registro, text="Limpiar casilleros", command=limpiar_campos)
            b4.place(x=375, y=160)
            b5 = Button(registro, text="Eliminar Registro", command=borrar)
            b5.place(x=500, y=160)

            registro.config(menu=menubar)

        def limpiar():
            textrecibo.delete(1.0, END)
            e_e1.set("0")
            e_e2.set("0")
            e_e3.set("0")
            e_e4.set("0")
            e_p1.set("0")
            e_p2.set("0")
            e_p3.set("0")
            e_p4.set("0")
            e_p5.set("0")
            e_p6.set("0")
            e_p7.set("0")
            e_p8.set("0")
            e_p9.set("0")
            e_p10.set("0")
            e_p11.set("0")
            e_b1.set("0")
            e_b2.set("0")
            e_b3.set("0")
            e_b4.set("0")
            e_b5.set("0")

            texte1.config(state=DISABLED)
            texte2.config(state=DISABLED)
            texte3.config(state=DISABLED)
            texte4.config(state=DISABLED)
            textp1.config(state=DISABLED)
            textp2.config(state=DISABLED)
            textp3.config(state=DISABLED)
            textp4.config(state=DISABLED)
            textp5.config(state=DISABLED)
            textp6.config(state=DISABLED)
            textp7.config(state=DISABLED)
            textp8.config(state=DISABLED)
            textp9.config(state=DISABLED)
            textp10.config(state=DISABLED)
            textp11.config(state=DISABLED)
            textb1.config(state=DISABLED)
            textb2.config(state=DISABLED)
            textb3.config(state=DISABLED)
            textb4.config(state=DISABLED)
            textb5.config(state=DISABLED)

            var1.set(0)
            var2.set(0)
            var3.set(0)
            var4.set(0)
            var5.set(0)
            var6.set(0)
            var7.set(0)
            var8.set(0)
            var9.set(0)
            var10.set(0)
            var11.set(0)
            var12.set(0)
            var13.set(0)
            var14.set(0)
            var15.set(0)
            var16.set(0)
            var17.set(0)
            var18.set(0)
            var19.set(0)
            var20.set(0)

            cevar.set('')
            cpvar.set('')
            cbvar.set('')
            imvar.set('')
            stvar.set('')
            ctvar.set('')

        def e1():
            if var1.get() == 1:
                texte1.config(state=NORMAL)
                texte1.delete(0, END)
                texte1.focus()
            else:
                texte1.config(state=DISABLED)
                e_e1.set('0')

        def e2():
            if var2.get() == 1:
                texte2.config(state=NORMAL)
                texte2.delete(0, END)
                texte2.focus()
            else:
                texte2.config(state=DISABLED)
                e_e2.set('0')

        def e3():
            if var3.get() == 1:
                texte3.config(state=NORMAL)
                texte3.delete(0, END)
                texte3.focus()
            else:
                texte3.config(state=DISABLED)
                e_e3.set('0')

        def e4():
            if var4.get() == 1:
                texte4.config(state=NORMAL)
                texte4.delete(0, END)
                texte4.focus()
            else:
                texte4.config(state=DISABLED)
                e_e4.set('0')

        def p1():
            if var5.get() == 1:
                textp1.config(state=NORMAL)
                textp1.delete(0, END)
                textp1.focus()
            else:
                textp1.config(state=DISABLED)
                e_p1.set('0')

        def p2():
            if var6.get() == 1:
                textp2.config(state=NORMAL)
                textp2.delete(0, END)
                textp2.focus()
            else:
                textp2.config(state=DISABLED)
                e_p2.set('0')

        def p3():
            if var7.get() == 1:
                textp3.config(state=NORMAL)
                textp3.delete(0, END)
                textp3.focus()
            else:
                textp3.config(state=DISABLED)
                e_p3.set('0')

        def p4():
            if var8.get() == 1:
                textp4.config(state=NORMAL)
                textp4.delete(0, END)
                textp4.focus()
            else:
                textp4.config(state=DISABLED)
                e_p4.set('0')

        def p5():
            if var9.get() == 1:
                textp5.config(state=NORMAL)
                textp5.delete(0, END)
                textp5.focus()
            else:
                textp5.config(state=DISABLED)
                e_p5.set('0')

        def p6():
            if var10.get() == 1:
                textp6.config(state=NORMAL)
                textp6.delete(0, END)
                textp6.focus()
            else:
                textp6.config(state=DISABLED)
                e_p6.set('0')

        def p7():
            if var11.get() == 1:
                textp7.config(state=NORMAL)
                textp7.delete(0, END)
                textp7.focus()
            else:
                textp7.config(state=DISABLED)
                e_p7.set('0')

        def p8():
            if var12.get() == 1:
                textp8.config(state=NORMAL)
                textp8.delete(0, END)
                textp8.focus()
            else:
                textp8.config(state=DISABLED)
                e_p8.set('0')

        def p9():
            if var13.get() == 1:
                textp9.config(state=NORMAL)
                textp9.delete(0, END)
                textp9.focus()
            else:
                textp9.config(state=DISABLED)
                e_p9.set('0')

        def p10():
            if var14.get() == 1:
                textp10.config(state=NORMAL)
                textp10.delete(0, END)
                textp10.focus()
            else:
                textp10.config(state=DISABLED)
                e_p10.set('0')

        def p11():
            if var15.get() == 1:
                textp11.config(state=NORMAL)
                textp11.delete(0, END)
                textp11.focus()
            else:
                textp11.config(state=DISABLED)
                e_p11.set('0')

        def b1():
            if var16.get() == 1:
                textb1.config(state=NORMAL)
                textb1.delete(0, END)
                textb1.focus()
            else:
                textb1.config(state=DISABLED)
                e_b1.set('0')

        def b2():
            if var17.get() == 1:
                textb2.config(state=NORMAL)
                textb2.delete(0, END)
                textb2.focus()
            else:
                textb2.config(state=DISABLED)
                e_b2.set('0')

        def b3():
            if var18.get() == 1:
                textb3.config(state=NORMAL)
                textb3.delete(0, END)
                textb3.focus()
            else:
                textb3.config(state=DISABLED)
                e_b3.set('0')

        def b4():
            if var19.get() == 1:
                textb4.config(state=NORMAL)
                textb4.delete(0, END)
                textb4.focus()
            else:
                textb4.config(state=DISABLED)
                e_b4.set('0')

        def b5():
            if var20.get() == 1:
                textb5.config(state=NORMAL)
                textb5.delete(0, END)
                textb5.focus()
            else:
                textb5.config(state=DISABLED)
                e_b5.set('0')

        def salir():
            valor = messagebox.askquestion("Salir", "Desea Salir del Sistema ")
            if valor == "yes":
                self.destroy()

        # FUNCIONES DE CAJA
        def comprobante():
            global fecha
            if cevar.get() != '' or cpvar.get() != '' or cbvar.get() != '':
                textrecibo.delete(1.0, END)
                x = random.randint(1,1000)
                orden = str(x)
                fecha = time.strftime('%d/%m/%Y')
                hora = time.strftime("%H:%M:%S")
                textrecibo.insert(END, 'LA CHIMBOTANA RESTAURANT\t \n')
                textrecibo.insert(END, 'Jr. Carlos de los Heros 388, Chimbote\t \n')
                textrecibo.insert(END, 'Celular: 933070855\n')
                textrecibo.insert(END, '------------------------------------------------------------------------\n')
                textrecibo.insert(END, '\tRUC:20606667109\t \n')
                textrecibo.insert(END, '------------------------------------------------------------------------\n')
                textrecibo.insert(END, 'BOLETA DE VENTA ELECTRÓNICA\t \n')
                textrecibo.insert(END, '------------------------------------------------------------------------\n')
                textrecibo.insert(END, f'Orden: {orden} \n')
                textrecibo.insert(END, 'Cajero: \n')
                textrecibo.insert(END, 'Cliente: \n')
                textrecibo.insert(END,  f'Fecha: {fecha} \n')
                textrecibo.insert(END, f'Hora: {hora} \n')
                textrecibo.insert(END, '------------------------------------------------------------------------\n')
                textrecibo.insert(END, 'Items:\t\t\t Costo del Item(S/.)\n')
                textrecibo.insert(END, '------------------------------------------------------------------------\n')

                if e_e1.get() != '0':
                    textrecibo.insert(END, f'Palta rellena\t\t\t\t{(int(e_e1.get())*5)}\n\n')

                if e_e2.get() != '0':
                    textrecibo.insert(END, f'Cebiche de pescado\t\t\t{(int(e_e2.get())*5)}\n\n')

                if e_e3.get() != '0':
                    textrecibo.insert(END, f'Chicharrón de pota\t\t\t{(int(e_e3.get())*5)}\n\n')

                if e_e4.get() != '0':
                    textrecibo.insert(END, f'Causa limeña\t\t\t\t{(int(e_e4.get())*5)}\n\n')

                if e_p1.get() != '0':
                    textrecibo.insert(END, f'Chicharrón de pollo\t\t\t{(int(e_p1.get())*13)}\n\n')

                if e_p2.get() != '0':
                    textrecibo.insert(END, f'Tallarín saltado de pollo\t\t{int(e_p2.get())*13}\n\n')

                if e_p3.get() != '0':
                    textrecibo.insert(END, f'Lomo saltado\t\t\t\t{int(e_p3.get())*14}\n\n')

                if e_p4.get() != '0':
                    textrecibo.insert(END, f'Arroz con mariscos\t\t\t{int(e_p4.get())*14}\n\n')

                if e_p5.get() != '0':
                    textrecibo.insert(END, f'Chicharrón de pescado\t\t\t{int(e_p5.get())*14}\n\n')

                if e_p6.get() != '0':
                    textrecibo.insert(END, f'Picante de mariscos\t\t\t{int(e_p6.get())*14}\n\n')

                if e_p7.get() != '0':
                     textrecibo.insert(END, f'Spaghetti a la huancaína\t\t{int(e_p7.get())*14}\n\n')

                if e_p8.get() != '0':
                     textrecibo.insert(END, f'Tallarines verdes con lomo\t\t{int(e_p8.get())*14}\n\n')

                if e_p9.get() != '0':
                     textrecibo.insert(END, f'Chicharrón a lo macho\t\t\t{int(e_p9.get())*15}\n\n')

                if e_p10.get() != '0':
                     textrecibo.insert(END, f'Tacu tacu a lo macho\t\t\t{int(e_p10.get())*15}\n\n')

                if e_p11.get() != '0':
                     textrecibo.insert(END, f'Picante de langostinos\t\t\t{int(e_p11.get())*15}\n\n')

                if e_b1.get() != '0':
                     textrecibo.insert(END, f'Limonada 1L\t\t\t\t{int(e_b1.get())*10}\n\n')

                if e_b2.get() != '0':
                     textrecibo.insert(END, f'Maracuyá 1L\t\t\t\t{int(e_b2.get())*10}\n\n')

                if e_b3.get() != '0':
                     textrecibo.insert(END, f'Chicha morada 1L\t\t\t{int(e_b3.get())*10}\n\n')

                if e_b4.get() != '0':
                     textrecibo.insert(END, f'Inka Cola 1L\t\t\t\t{int(e_b4.get())*8}\n\n')

                if e_b5.get() != '0':
                     textrecibo.insert(END, f'Coca Cola 1L\t\t\t\t{int(e_b5.get())*8}\n\n')

                textrecibo.insert(END, '------------------------------------------------------------------------\n')

                if cevar.get() != 'S/. 0.00':
                    textrecibo.insert(END, f'Costo Entradas\t\t\tS/. {precio_Entrada:.2f}\n\n')
                if cpvar.get() != 'S/. 0.00':
                    textrecibo.insert(END, f' Costo Menú\t\t\tS/. {precio_Fondo:.2f}\n\n')
                if cbvar.get() != 'S/. 0.00':
                    textrecibo.insert(END, f' Costo Bebidas\t\t\t S/. {precio_Bebida:.2f}\n\n')

                textrecibo.insert(END, f' SUBTOTAL\t\t\tS/. {sub_total:.2f}\n\n')
                textrecibo.insert(END, f' IGV 18%\t\t\tS/. {impuesto:.2f}\n\n')
                textrecibo.insert(END, f' IMPORTE TOTAL\t\t\tS/. {sub_total+impuesto:.2f}\n\n')
                textrecibo.insert(END, '-----------------------------------------------------------------------\n')
                textrecibo.insert(END, ' MUCHAS GRACIAS POR SU COMPRA\n')
            else:
                messagebox.showerror('Error', 'No hay items seleccionados')

        def guardar():
            if textrecibo.get(1.0, END) == '\n':
                pass
            else:
                url = filedialog.asksaveasfile(mode='w', defaultextension='.txt')
                if url == None:
                    pass
                else:
                    comprobante_data = textrecibo.get(1.0, END)
                    url.write(comprobante_data)
                    url.close()
                    messagebox.showinfo('Información', 'El comprobante se ha guardado exitosamente')

        def mostrar_tarifa():
            tarifa = Toplevel()
            tarifa.title('Tarifas de Delivery')
            tarifa.resizable(0, 0)
            tarifa.config(bg='khaki1')

            texto_09 = "Por ubicacion de urbanizaciones\n\n"
            texto_10 = "Urbanización la caleta\n"
            texto_11 = "Urbanización el progreso\n"
            texto_12 = "Urbanización 21 de Abril\n"
            texto_13 = "Urbanización el acero\n\n"
            texto_14 = "\ts/. 5.00\n\n"
            texto_15 = "Urbanización Los Pinos\n"
            texto_16 = "Urbanización Nueva Generación\n"
            texto_17 = "Urbanización El Carmen\n\n"
            texto_18 = "\ts/. 6.00\n\n"
            texto_19 = "Urbanización Industrial Gran Trapecio\n"
            texto_20 = "Urbanización Industrial 27 de Octubre\n\n"
            texto_21 = "\ts/. 7.00\n\n"
            texto_22 = "Urbanización Industrial Villa Maria\n"
            texto_23 = "Urbanización Industrial 1 de Mayo\n"
            texto_24 = "Urbanización Industrial Santa Angela\n\n"
            texto_25 = "\ts/. 9.00\n"

            titulo =Label(tarifa, text="\nCOSTO DE DELIVERY EN CHIMBOTE\n", font=('arial', 14, 'bold'), bg='khaki1')
            titulo.grid(row=0, column=0)

            texto = Label(tarifa, bg='khaki1', font=('arial', 12),
                          text= texto_09 + texto_10 + texto_11 + texto_12 + texto_13 + texto_14 + texto_15 + texto_16
                                + texto_17 + texto_18 + texto_19 + texto_20 +  texto_21 + texto_22 + texto_23
                                + texto_24 + texto_25 + "\n")
            texto.grid(row=1, column=0)

        #CHECKBUTTON DE LAS ENTRADAS
        e1 = Checkbutton(entrada_frame, text='Palta rellena', font=('arial', 12, 'bold'), onvalue=1, offvalue=0,
                         variable=var1, command=e1)
        e1.grid(row=0, column=0, sticky=W)

        e2 = Checkbutton(entrada_frame, text='Cebiche de pescado', font=('arial', 12, 'bold'), onvalue=1, offvalue=0,
                         variable=var2, command=e2)
        e2.grid(row=1, column=0, sticky=W)

        e3 = Checkbutton(entrada_frame, text='Chicharrón de pota', font=('arial', 12, 'bold'), onvalue=1, offvalue=0,
                         variable=var3, command=e3)
        e3.grid(row=2, column=0, sticky=W)

        e4 = Checkbutton(entrada_frame, text='Causa limeña', font=('arial', 12, 'bold'), onvalue=1, offvalue=0,
                         variable=var4, command=e4)
        e4.grid(row=3, column=0, sticky=W)

        # ENTRIES DE LAS ENTRADAS
        texte1 = Entry(entrada_frame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_e1)
        texte1.grid(row=0, column=1)

        texte2 = Entry(entrada_frame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_e2)
        texte2.grid(row=1, column=1)

        texte3 = Entry(entrada_frame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_e3)
        texte3.grid(row=2, column=1)

        texte4 = Entry(entrada_frame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_e4)
        texte4.grid(row=3, column=1)

        # CHECKBUTTON DEL MENÚ
        p1 = Checkbutton(fondo_frame, text='Chicharrón de pollo', font=('arial', 12, 'bold'), onvalue=1, offvalue=0,
                         variable=var5, command=p1)
        p1.grid(row=0, column=2, sticky=W)

        p2 = Checkbutton(fondo_frame, text='Tallarín saltado de pollo', font=('arial', 12, 'bold'), onvalue=1,
                         offvalue=0, variable=var6, command=p2)
        p2.grid(row=1, column=2, sticky=W)

        p3 = Checkbutton(fondo_frame, text='Lomo saltado', font=('arial', 12, 'bold'), onvalue=1, offvalue=0,
                         variable=var7, command=p3)
        p3.grid(row=2, column=2, sticky=W)

        p4 = Checkbutton(fondo_frame, text='Arroz con mariscos', font=('arial', 12, 'bold'), onvalue=1, offvalue=0,
                         variable=var8, command=p4)
        p4.grid(row=3, column=2, sticky=W)

        p5 = Checkbutton(fondo_frame, text='Chicharrón de pescado', font=('arial', 12, 'bold'), onvalue=1, offvalue=0,
                         variable=var9, command=p5)
        p5.grid(row=4, column=2, sticky=W)

        p6 = Checkbutton(fondo_frame, text='Picante de mariscos', font=('arial', 12, 'bold'), onvalue=1, offvalue=0,
                         variable=var10, command=p6)
        p6.grid(row=5, column=2, sticky=W)

        p7 = Checkbutton(fondo_frame, text='Spaghetti a la huancaína', font=('arial', 12, 'bold'), onvalue=1,
                         offvalue=0, variable=var11, command=p7)
        p7.grid(row=6, column=2, sticky=W)

        p8 = Checkbutton(fondo_frame, text='Tallarines verdes con lomo', font=('arial', 12, 'bold'), onvalue=1,
                         offvalue=0, variable=var12, command=p8)
        p8.grid(row=7, column=2, sticky=W)

        p9 = Checkbutton(fondo_frame, text='Chicharrón a lo macho', font=('arial', 12, 'bold'), onvalue=1, offvalue=0,
                         variable=var13, command=p9)
        p9.grid(row=8, column=2, sticky=W)

        p10 = Checkbutton(fondo_frame, text='Tacu tacu a lo macho', font=('arial', 12, 'bold'), onvalue=1, offvalue=0,
                          variable=var14, command=p10)
        p10.grid(row=9, column=2, sticky=W)

        p11 = Checkbutton(fondo_frame, text='Picante de langostinos', font=('arial', 12, 'bold'), onvalue=1, offvalue=0,
                          variable=var15, command=p11)
        p11.grid(row=10, column=2, sticky=W)

        # ENTRIES DEL MENÚ
        textp1 = Entry(fondo_frame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_p1)
        textp1.grid(row=0, column=3)

        textp2 = Entry(fondo_frame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_p2)
        textp2.grid(row=1, column=3)

        textp3 = Entry(fondo_frame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_p3)
        textp3.grid(row=2, column=3)

        textp4 = Entry(fondo_frame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_p4)
        textp4.grid(row=3, column=3)

        textp5 = Entry(fondo_frame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_p5)
        textp5.grid(row=4, column=3)

        textp6 = Entry(fondo_frame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_p6)
        textp6.grid(row=5, column=3)

        textp7 = Entry(fondo_frame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_p7)
        textp7.grid(row=6, column=3)

        textp8 = Entry(fondo_frame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_p8)
        textp8.grid(row=7, column=3)

        textp9 = Entry(fondo_frame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_p9)
        textp9.grid(row=8, column=3)

        textp10 = Entry(fondo_frame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_p10)
        textp10.grid(row=9, column=3)

        textp11 = Entry(fondo_frame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_p11)
        textp11.grid(row=10, column=3)

        # CHECKBUTTON DE LAS BEBIDAS
        b1 = Checkbutton(bebida_frame, text='Limonada 1L', font=('arial', 12, 'bold'), onvalue=1, offvalue=0,
                         variable=var16, command=b1)
        b1.grid(row=0, column=4, sticky=W)

        b2 = Checkbutton(bebida_frame, text='Maracuyá 1L', font=('arial', 12, 'bold'), onvalue=1, offvalue=0,
                         variable=var17, command=b2)
        b2.grid(row=1, column=4, sticky=W)

        b3 = Checkbutton(bebida_frame, text='Chicha morada 1L', font=('arial', 12, 'bold'), onvalue=1, offvalue=0,
                         variable=var18, command=b3)
        b3.grid(row=2, column=4, sticky=W)

        b4 = Checkbutton(bebida_frame, text='Inka Cola 1L', font=('arial', 12, 'bold'), onvalue=1, offvalue=0,
                         variable=var19, command=b4)
        b4.grid(row=3, column=4, sticky=W)

        b5 = Checkbutton(bebida_frame, text='Coca Cola 1L', font=('arial', 12, 'bold'), onvalue=1, offvalue=0,
                         variable=var20, command=b5)
        b5.grid(row=4, column=4, sticky=W)

        # ENTRIES DE LAS BEBIDAS
        textb1 = Entry(bebida_frame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_b1)
        textb1.grid(row=0, column=5)

        textb2 = Entry(bebida_frame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_b2)
        textb2.grid(row=1, column=5)

        textb3 = Entry(bebida_frame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_b3)
        textb3.grid(row=2, column=5)

        textb4 = Entry(bebida_frame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_b4)
        textb4.grid(row=3, column=5)

        textb5 = Entry(bebida_frame, font=('arial', 12, 'bold'), bd=7, width=6, state=DISABLED, textvariable=e_b5)
        textb5.grid(row=4, column=5)

        # LABEL, ENTRY DE LOS COSTOS, SUBTOTAL, IMPUESTO E IMPORTE TOTAL
        label_costodeentrada = Label(costo_frame, text='Costo de Entradas', font=('arial', 14, 'bold'), fg='white',
                                     bg='DodgerBlue4')
        label_costodeentrada.grid(row=0, column=0)
        textcostodeentrada = Entry(costo_frame, font=('arial', 12, 'bold'), bd=6, width=14, state='readonly',
                                   textvariable=cevar)
        textcostodeentrada.grid(row=0, column=1, padx=62)

        label_costodeplato = Label(costo_frame, text='Costo de Platos', font=('arial', 14, 'bold'), fg='white',
                                   bg='DodgerBlue4')
        label_costodeplato.grid(row=1, column=0)
        textcostodeplato = Entry(costo_frame, font=('arial', 12, 'bold'), bd=6, width=14, state='readonly',
                                 textvariable=cpvar)
        textcostodeplato.grid(row=1, column=1, padx=64)

        label_costodebebida = Label(costo_frame, text='Costo de Bebidas', font=('arial', 14, 'bold'), fg='white',
                                    bg='DodgerBlue4')
        label_costodebebida.grid(row=2, column=0)
        textcostodebebida = Entry(costo_frame, font=('arial', 12, 'bold'), bd=6, width=14, state='readonly',
                                  textvariable=cbvar)
        textcostodebebida.grid(row=2, column=1, padx=62)

        label_subtotal = Label(costo_frame, text='Sub Total', font=('arial', 14, 'bold'), fg='white', bg='DodgerBlue4')
        label_subtotal.grid(row=0, column=2)
        textsubtotal = Entry(costo_frame, font=('arial', 12, 'bold'), bd=6, width=14, state='readonly',
                             textvariable=stvar)
        textsubtotal.grid(row=0, column=3, padx=62)

        label_sertax = Label(costo_frame, text='Total IGV', font=('arial', 14, 'bold'), fg='white', bg='DodgerBlue4')
        label_sertax.grid(row=1, column=2)
        textsertax = Entry(costo_frame, font=('arial', 12, 'bold'), bd=6, width=14, state='readonly',
                           textvariable=imvar)
        textsertax.grid(row=1, column=3, padx=62)

        label_costotal = Label(costo_frame, text='Importe Total', font=('arial', 14, 'bold'), fg='white',
                               bg='DodgerBlue4')
        label_costotal.grid(row=2, column=2)
        textcostotal = Entry(costo_frame, font=('arial', 12, 'bold'), bd=6, width=14, state='readonly',
                             textvariable=ctvar)
        textcostotal.grid(row=2, column=3, padx=62)

        # BOTONES
        boton_total = Button(pedido_frame, text='Total', font=('arial', 12, 'bold'), fg='white', bg='sandy brown',
                             bd=3,padx=15, command=bt_total)
        boton_total.grid(row=0, column=0)

        boton_registrar = Button(pedido_frame, text='Registrar', font=('arial', 13, 'bold'), fg='white',
                                 bg='sandy brown', bd=3, padx=13, command=registrar)
        boton_registrar.grid(row=0, column=1)

        boton_limpiar = Button(pedido_frame, text='Limpiar', font=('arial', 12, 'bold'), fg='white', bg='salmon', bd=3,
                               padx=10, command=limpiar)
        boton_limpiar.grid(row=0, column=2)

        boton_salir = Button(pedido_frame, text='Salir', font=('arial', 13, 'bold'), fg='white', bg='salmon', bd=3,
                             padx=15, command=salir)
        boton_salir.grid(row=0, column=3)

        boton_comprobante = Button(caja_frame, text='Comprobante', font=('arial', 12, 'bold'), fg='white'
                                   , bg='salmon', bd=3, padx=5, command=comprobante)
        boton_comprobante.grid(row=0, column=0)

        boton_guardar = Button(caja_frame, text='Guardar', font=('arial', 13, 'bold'), fg='white', bg='salmon', bd=3,
                               padx=5, command=guardar)
        boton_guardar.grid(row=0, column=1)

        boton_tarifa= Button(caja_frame, text='Tarifas', font=('arial', 13, 'bold'), fg='white', bg='sandy brown', bd=3,
                               padx=5, command=mostrar_tarifa)
        boton_tarifa.grid(row=0, column=2)

        #TEXTO DE BOLETA
        textrecibo = Text(recibo_frame, font=('arial', 12, 'bold'), bd=3, width=40, height=20)
        textrecibo.grid(row=0, column=0, sticky=W)
