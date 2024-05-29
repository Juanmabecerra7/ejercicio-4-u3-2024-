from Publicaciones import Publicaciones
import datetime as date

class Libro(Publicaciones):
    __nom_autor = str
    __fecha_edicion = str
    __cant_pag = int
    
    def __init__ (self,titulo,categoria,precio,nom_autor,fecha_edicion, cant_pag):
        super().__init__(titulo,categoria,precio)
        self.__nom_autor = nom_autor
        self.__fecha_edicion = fecha_edicion
        self.__cant_pag = cant_pag
        
    def getNom_Autor (self):
        return self.__nom_autor
    def getFecha_Edicion (self):
        return self.__fecha_edicion
    def getCant_Pag (self):
        return self.__cant_pag
    def ImporteVenta (self):
        anios_antiguedad = date.now().year - self.__fecha_edicion
        descuento = self.__precio * (0.01 * anios_antiguedad)
        return self.__precio - descuento
    def mostrar(self):
        print("Libro Fisico")
        super().mostrar()
        #print(f"Importe de Venta: {self.ImporteVenta()}")
