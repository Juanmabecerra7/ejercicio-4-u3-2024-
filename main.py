from Lista import Lista

if __name__ == "__main__":
    l = Lista()
    l.cargarPublicaciones()
    while True:
        print("---Menu de Opciones---")
        print("1: Agregar publicaciones a la colección")
        print("2: Mostrar que tipo de publicacion se encuentra en dicha posicion")
        print("3: Mostrar la cantidad de publicaciones de cada tipo")
        print("4: Mostrar los datos para todas las publicaciones ")
        print("5: Salir")
        opcion = int(input("Ingrese la opcion deseada: "))
        if opcion == 1:
            l.agregar_publicacion()
        elif opcion == 2:
            pass
        elif opcion == 3:
            l.mostrarCantidad()
        elif opcion == 4:
            l.recorrer()
        elif opcion == 5:
            exit()
        else:
            print("---OPCION INCORRECTA---")
