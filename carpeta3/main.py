import tkinter as tk
from cliente.vista import Frame,barrita_menu

def main(): 
    ventana = tk.Tk()
    ventana.title('Listado Peliculas')
    ventana.iconbitmap('img/videocamara.ico')
    ventana.resizable(False,False)

    barrita_menu(ventana)
    app = Frame(root=ventana)

    ventana.mainloop()
    
if __name__ == '__main__':
    main()
