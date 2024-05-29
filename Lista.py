from Nodo import Nodo
from Publicaciones import Publicaciones
from AudioLibro import AudioLibro
from Libro import Libro
import csv

class Lista:
    __comienzo: Nodo
    __actual: Nodo
    __indice: int
    __tope: int
    
    def __init__(self):
        self.__comienzo=None
        self.__actual=None
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.__indice==self.__tope:
            self.__actual=self.__comienzo
            self.__indice=0
            raise StopIteration
        else:
            self.__indice+=1
            dato = self.__actual.getDato()
            self.__actual=self.__actual.getSiguiente()
            return dato
        
    def cargarPublicaciones (self):
        self.cargarAudioLibro()
        self.cargarLibro()
        
    def agregarPublicacion(self, unaPublicacion):
        nodo = Nodo(unaPublicacion)
        nodo.setSiguiente(self.__comienzo)
        self.__comienzo=nodo
        self.__actual=nodo
        #self.__tope+=1
        
        
    def cargarAudioLibro (self):
        archivo = open("AudioLibro.csv")
        reader = csv.reader(archivo,delimiter=";")
        for fila in reader:
            titulo = fila[0]
            categoria = fila[1]
            precio = float(fila[2])
            tiempo = int(fila[3])
            nom_narrador = fila[4]
            unaPublicacion = AudioLibro(titulo,categoria,precio,tiempo,nom_narrador)
            self.agregarPublicacion(unaPublicacion)
        archivo.close()
    
    def cargarLibro (self):
        archivo = open("libro.csv")
        reader = csv.reader(archivo,delimiter=";")
        for fila in reader:
            titulo = fila[0]
            categoria = fila[1]
            precio = float(fila[2])
            nom_autor = fila[3]
            fecha_edicion = fila[4]
            cant_pag = int(fila[5])
            unaPublicacion = Libro (titulo,categoria,precio,nom_autor,fecha_edicion,cant_pag)
            self.agregarPublicacion(unaPublicacion)
        archivo.close()
            
    def agregar_publicacion(self):
        tipo = input("Ingrese el tipo de publicación (libro/audio): ").strip().lower()
        titulo = input("Ingrese el título: ").strip()
        categoria = input("Ingrese la categoría: ").strip()
        precio = float(input("Ingrese el precio base: ").strip())
        if tipo == "libro":
            nom_autor = input("Ingrese el nombre del autor: ").strip()
            fecha_edicion = int(input("Ingrese el año de edición: ").strip())
            cant_pag = int(input("Ingrese la cantidad de páginas: ").strip())
            unaPublicacion = Libro(titulo, categoria, precio, nom_autor, fecha_edicion, cant_pag)
            self.agregarPublicacion(unaPublicacion)
            print("Se agrego correctamente")
        elif tipo == "audio":
            tiempo = int(input("Ingrese el tiempo de reproduccion en minutos: "))
            nom_narrador = input("Ingrese el nombre del narrador: ").strip()
            unaPublicacion = AudioLibro(titulo, categoria, precio, tiempo,nom_narrador)
            self.agregarPublicacion(unaPublicacion)
            print("Se agrego correctamente")
        else:
            print("Tipo de publicación no válido.")
        
    
    def mostrarCantidad (self):
        aux = self.__comienzo
        cantL = 0
        cantAL = 0
        while aux != None:
            if isinstance(aux.getDato(),Libro):
                cantL += 1
            elif isinstance(aux.getDato(),AudioLibro):
                cantAL += 1
            aux = aux.getSiguiente()
        print (f"la cantidad de libros son: {cantL}, y Audio libro son: {cantAL}")
        
    def recorrer (self):
        aux = self.__comienzo
        while aux != None:
            if isinstance(aux.getDato(),Libro):
                Libro.mostrar(aux.getDato())
            elif isinstance(aux.getDato(),AudioLibro):
                AudioLibro.mostrar(aux.getDato())
            aux = aux.getSiguiente()