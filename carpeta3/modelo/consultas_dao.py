from .connecciondb import Conneccion

def crear_tabla():
    conn = Conneccion()

    sql = '''
        CREATE TABLE IF NOT EXISTS Genero(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Nombre VARCHAR(50)
        );
        
        CREATE TABLE IF NOT EXISTS Autores(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Nombre VARCHAR(100)
        );
        
        CREATE TABLE IF NOT EXISTS Peliculas(
        ID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        Nombre VARCHAR(150),
        Duracion VARCHAR(4),
        Genero INTEGER,
        Autor INTEGER,
        Anio VARCHAR(4),
        FOREIGN KEY (Genero) REFERENCES Genero(ID),
        FOREIGN KEY (Autor) REFERENCES Autores(Nombres))
        );
    '''
    
    try:
        # Usamos executescript para ejecutar múltiples declaraciones SQL
        conn.cursor.executescript(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error creando tablas: {e}")

class Peliculas:

    def __init__(self, nombre, duracion, genero, autor, anio):
        self.nombre = nombre
        self.duracion = duracion
        self.genero = genero
        self.autor = autor
        self.anio = anio

    def __str__(self):
        return f'Pelicula[{self.nombre}, {self.duracion}, {self.genero}, {self.autor}, {self.anio}]'

def guardar_peli(pelicula):
    conn = Conneccion()

    sql = '''
        INSERT INTO Peliculas (Nombre, Duracion, Genero, Autor, Anio)
        VALUES (?, ?, ?, ?, ?);
    '''
    try:
        conn.cursor.execute(sql, (pelicula.nombre, pelicula.duracion, pelicula.genero, pelicula.autor, pelicula.anio))
        conn.cerrar_con()
    except Exception as e:
        print(f"Error guardando película: {e}")

def listar_peli():
    conn = Conneccion()
    listar_peliculas = []

    sql = f'''
        SELECT * FROM Peliculas as p 
        INNER JOIN Genero as g ON p.Genero = g.ID
        INNER JOIN Autores as a ON p.Autor = a.ID;
    '''
    try:
        conn.cursor.execute(sql)
        listar_peliculas = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_peliculas
    except :
        pass

def listar_generos():
    conn = Conneccion()
    listar_genero = []

    sql = f'''
        SELECT * FROM Genero;
    '''
    try:
        conn.cursor.execute(sql)
        listar_genero = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_genero
    except :
        pass

def listar_autores():
    conn = Conneccion()
    listar_autores = []

    sql = '''
        SELECT * FROM Autores;
    '''
    try:
        conn.cursor.execute(sql)
        listar_autores = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_autores
    except :
        pass

def editar_peli(pelicula, id):
    conn = Conneccion()

    sql = f'''
        UPDATE Peliculas
        SET Nombre ='{pelicula.nombre}', Duracion = '{pelicula.duracion}', Genero = {pelicula.genero}, Autor ='{pelicula.autor}', Anio = '{pelicula.anio}'
        WHERE ID = {id};
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except :
        pass

def borrar_peli(id):
    conn = Conneccion()

    sql = f'''
        DELETE FROM Peliculas
        WHERE ID = {id};
    '''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except :
        pass

# Ejecuta las funciones para crear las tablas y agregar datos de ejemplo al inicio
#crear_tabla()
#insertar_datos_ejemplo()
