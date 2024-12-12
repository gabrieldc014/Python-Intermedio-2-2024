import tkinter as tk
from tkinter import ttk
from modelo.consultas_dao import Peliculas, crear_tabla, guardar_peli, listar_peli, listar_generos, editar_peli, borrar_peli

class Frame(tk.Frame):
    def __init__(self, root=None):
        super().__init__(root, width=480, height=320)
        self.root = root
        self.id_peli = None
        self.pack()

        self.label_form()
        self.input_form()
        self.botones_principales()
        self.bloquear_campos()
        self.mostrar_tabla()

    def label_form(self):
        labels = ["Nombre", "Duración", "Género", "Autor", "Año"]
        for i, text in enumerate(labels):
            label = tk.Label(self, text=f"{text}: ")
            label.config(font=('Arial', 12, 'bold'))
            label.grid(row=i, column=0, padx=10, pady=10)

    def input_form(self):
        self.nombre = tk.StringVar()
        self.entry_nombre = tk.Entry(self, textvariable=self.nombre)
        self.entry_nombre.config(width=50)
        self.entry_nombre.grid(row=0, column=1, padx=10, pady=10)

        self.duracion = tk.StringVar()
        self.entry_duracion = tk.Entry(self, textvariable=self.duracion)
        self.entry_duracion.config(width=50)
        self.entry_duracion.grid(row=1, column=1, padx=10, pady=10)

        self.generos = ['Seleccione Uno'] + [i[1] for i in listar_generos()]
        self.entry_genero = ttk.Combobox(self, state="readonly")
        self.entry_genero['values'] = self.generos
        self.entry_genero.current(0)
        self.entry_genero.config(width=25)
        self.entry_genero.bind("<<ComboboxSelected>>")
        self.entry_genero.grid(row=2, column=1, padx=10, pady=10)

        self.autor = tk.StringVar()
        self.entry_autor = tk.Entry(self, textvariable=self.autor)
        self.entry_autor.config(width=50)
        self.entry_autor.grid(row=3, column=1, padx=10, pady=10)

        self.anio = tk.StringVar()
        self.entry_anio = tk.Entry(self, textvariable=self.anio)
        self.entry_anio.config(width=50)
        self.entry_anio.grid(row=4, column=1, padx=10, pady=10)

    def botones_principales(self):
        self.btn_alta = tk.Button(self, text='Nuevo', command=self.habilitar_campos)
        self.btn_alta.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B', cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_alta.grid(row=5, column=0, padx=10, pady=10)

        self.btn_modi = tk.Button(self, text='Guardar', command=self.guardar_campos)
        self.btn_modi.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#0D2A83', cursor='hand2', activebackground='#7594F5', activeforeground='#000000')
        self.btn_modi.grid(row=5, column=1, padx=10, pady=10)

        self.btn_cance = tk.Button(self, text='Cancelar', command=self.bloquear_campos)
        self.btn_cance.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A', cursor='hand2', activebackground='#F35B5B', activeforeground='#000000')
        self.btn_cance.grid(row=5, column=2, padx=10, pady=10)

    def guardar_campos(self):
        pelicula = Peliculas(
            self.nombre.get(),
            self.duracion.get(),
            self.entry_genero.current(),
            self.autor.get(),
            self.anio.get()
        )

        if self.id_peli is None:
            guardar_peli(pelicula)
        else:
            editar_peli(pelicula, int(self.id_peli))

        self.bloquear_campos()
        self.mostrar_tabla()

    def habilitar_campos(self):
        self.entry_nombre.config(state='normal')
        self.entry_duracion.config(state='normal')
        self.entry_genero.config(state='normal')
        self.entry_autor.config(state='normal')
        self.entry_anio.config(state='normal')
        self.btn_modi.config(state='normal')
        self.btn_cance.config(state='normal')
        self.btn_alta.config(state='disabled')

    def bloquear_campos(self):
        self.entry_nombre.config(state='disabled')
        self.entry_duracion.config(state='disabled')
        self.entry_genero.config(state='disabled')
        self.entry_autor.config(state='disabled')
        self.entry_anio.config(state='disabled')
        self.btn_modi.config(state='disabled')
        self.btn_cance.config(state='disabled')
        self.btn_alta.config(state='normal')
        self.nombre.set('')
        self.duracion.set('')
        self.entry_genero.current(0)
        self.autor.set('')
        self.anio.set('')
        self.id_peli = None

    def mostrar_tabla(self):
        self.lista_p = listar_peli()
        self.lista_p.reverse()

        self.tabla = ttk.Treeview(self, columns=('Nombre', 'Duración', 'Género', 'Autor', 'Año'))
        self.tabla.grid(row=6, column=0, columnspan=4, sticky='nse')

        self.scroll = ttk.Scrollbar(self, orient='vertical', command=self.tabla.yview)
        self.scroll.grid(row=6, column=4, sticky='nse')
        self.tabla.configure(yscrollcommand=self.scroll.set)

        self.tabla.heading('#0', text='ID')
        self.tabla.heading('#1', text='Nombre')
        self.tabla.heading('#2', text='Duración')
        self.tabla.heading('#3', text='Género')
        self.tabla.heading('#4', text='Autor')
        self.tabla.heading('#5', text='Año')

        for p in self.lista_p:
            self.tabla.insert('',0, text=p[0], 
                              values=(p[1], p[2], p[3], p[4], p[5]))

        self.btn_editar = tk.Button(self, text='Editar', command=self.editar_registro)
        self.btn_editar.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#1C500B', cursor='hand2', activebackground='#3FD83F', activeforeground='#000000')
        self.btn_editar.grid(row=7, column=0, padx=10, pady=10)

        self.btn_delete = tk.Button(self, text='Eliminar', command=self.eliminar_registro)
        self.btn_delete.config(width=20, font=('Arial', 12, 'bold'), fg='#FFFFFF', bg='#A90A0A', cursor='hand2', activebackground='#F35B5B', activeforeground='#000000')
        self.btn_delete.grid(row=7, column=1, padx=10, pady=10)

    def editar_registro(self):
        try:
            self.id_peli = self.tabla.item(self.tabla.selection())['text']
            self.nombre_peli = self.tabla.item(self.tabla.selection())['values'][0]
            self.dura_peli = self.tabla.item(self.tabla.selection())['values'][1]
            self.gene_peli = self.tabla.item(self.tabla.selection())['values'][2]
            self.autor_peli = self.tabla.item(self.tabla.selection())['values'][3]
            self.anio_peli = self.tabla.item(self.tabla.selection())['values'][4]

            self.habilitar_campos()
            self.nombre.set(self.nombre_peli)
            self.duracion.set(self.dura_peli)
            self.entry_genero.current(self.generos.index(self.gene_peli))
            self.autor.set(self.autor_peli)
            self.anio.set(self.anio_peli)
        except IndexError as e:
            print(f"Error al editar registro: {e}")

    def eliminar_registro(self):
        self.id_peli = self.tabla.item(self.tabla.selection())['text']
        borrar_peli(int(self.id_peli))
        self.mostrar_tabla()


def barrita_menu(root):
    barra = tk.Menu(root)
    root.config(menu=barra, width=300, height=300)
    menu_inicio = tk.Menu(barra, tearoff=0)
    menu_inicio2 = tk.Menu(barra, tearoff=0)

    barra.add_cascade(label='Inicio', menu=menu_inicio)
    barra.add_cascade(label='Consultas', menu=menu_inicio)
    barra.add_cascade(label='Acerca de..', menu=menu_inicio)
    barra.add_cascade(label='Ayuda', menu=menu_inicio2)

    menu_inicio.add_command(label='Conectar DB', command=crear_tabla)
    menu_inicio.add_command(label='Desconectar DB')  
    menu_inicio.add_command(label='Salir', command= root.destroy)
    # Menú "Ayuda"
    menu_inicio2.add_command(label='Contáctanos')
    menu_inicio2.add_command(label='Manual')
    menu_inicio2.add_command(label='Acerca del software')
