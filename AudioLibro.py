from Publicaciones import Publicaciones

class AudioLibro(Publicaciones):
    __tiempo = int
    __nom_narrador = str
    
    def __init__ (self,titulo,categoria,precio,tiempo,nom_narrador):
        super().__init__(titulo,categoria,precio)
        self.__tiempo = tiempo
        self.__nom_narrador = nom_narrador
        
    def getTiempo (self):
        return self.__tiempo
    def getNom_Narrador (self):
        return self.__nom_narrador
    def ImporteVenta (self):
        porcentaje = super().getPrecio() / 10
        imp = super().getPrecio() + porcentaje
        return imp
    def mostrar (self):
        print("Audio Libro")
        super().mostrar()
        print(f"Importe de Venta: {self.ImporteVenta()}")

    