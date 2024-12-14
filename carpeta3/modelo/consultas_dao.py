from .connecciondb import Conneccion

def crear_tabla():
    conn = Conneccion()

    sql= '''
        CREATE TABLE IF NOT EXISTS Directores(
        ID INTEGER NOT NULL,
        Nombre VARCHAR(100),
        Nacionalidad VARCHAR(50),
        PRIMARY KEY (ID AUTOINCREMENT)
        );

        CREATE TABLE IF NOT EXISTS Genero(
        ID INTEGER NOT NULL,
        Nombre VARCHAR(50),
        PRIMARY KEY (ID AUTOINCREMENT)
        );

        CREATE TABLE IF NOT EXISTS Peliculas(
        ID INTEGER NOT NULL,
        Nombre VARCHAR(150),
        Duracion VARCHAR(4),
        Genero INTEGER,
        Director INTEGER,
        Ano INTEGER,
        PRIMARY KEY (ID AUTOINCREMENT),
        FOREIGN KEY (Genero) REFERENCES Genero(ID),
        FOREIGN KEY (Director) REFERENCES Directores(ID)
        );
'''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error creating tables: {e}")


class Peliculas():
    def __init__(self, nombre, duracion, genero, director, ano):
       self.nombre = nombre
       self.duracion = duracion
       self.genero = genero
       self.director = director
       self.ano = ano

    def __str__(self):
        return f'Pelicula[{self.nombre},{self.duracion},{self.genero},{self.director},{self.ano}]'

def guardar_peli(pelicula):
    conn = Conneccion()

    sql= f'''
        INSERT INTO Peliculas(Nombre, Duracion, Genero, Director, Ano)
        VALUES('{pelicula.nombre}','{pelicula.duracion}',{pelicula.genero},{pelicula.director},{pelicula.ano});
'''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error saving movie: {e}")

def listar_peli():
    conn = Conneccion()
    listar_peliculas = []

    sql= f'''
        SELECT p.*, g.Nombre as GeneroNombre, d.Nombre as DirectorNombre 
        FROM Peliculas as p
        INNER JOIN Genero as g ON p.Genero = g.ID
        INNER JOIN Directores as d ON p.Director = d.ID;
'''
    try:
        conn.cursor.execute(sql)
        listar_peliculas = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_peliculas
    except Exception as e:
        print(f"Error listing movies: {e}")
        return []

def listar_generos():
    conn = Conneccion()
    listar_genero = []

    sql= f'''
        SELECT * FROM Genero;
'''
    try:
        conn.cursor.execute(sql)
        listar_genero = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_genero
    except Exception as e:
        print(f"Error listing genres: {e}")
        return []

def listar_directores():
    conn = Conneccion()
    listar_director = []

    sql= f'''
        SELECT * FROM Directores;
'''
    try:
        conn.cursor.execute(sql)
        listar_director = conn.cursor.fetchall()
        conn.cerrar_con()

        return listar_director
    except Exception as e:
        print(f"Error listing directors: {e}")
        return []

def editar_peli(pelicula, id):
    conn = Conneccion()

    sql= f'''
        UPDATE Peliculas
        SET Nombre = '{pelicula.nombre}', 
            Duracion = '{pelicula.duracion}', 
            Genero = {pelicula.genero},
            Director = {pelicula.director},
            Ano = {pelicula.ano}
        WHERE ID = {id}
        ;
'''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error editing movie: {e}")

def borrar_peli(id):
    conn = Conneccion()

    sql= f'''
        DELETE FROM Peliculas
        WHERE ID = {id}
        ;
'''
    try:
        conn.cursor.execute(sql)
        conn.cerrar_con()
    except Exception as e:
        print(f"Error deleting movie: {e}")