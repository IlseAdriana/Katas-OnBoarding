from black import err


def main():
    try:
        configuration = open('config.txt')
    except FileNotFoundError:
        print("No se encontro el archivo config.txt")
    except IsADirectoryError:
        print("Se encontro config.txt, pero es un directorio, por lo que no se pudo leer") 
    except (BlockingIOError, TimeoutError):
        print("Sistema de archivos bajo carga pesada, no se pudo completar la lectura del archivo de configuración")

if __name__ == '__main__':
    main()
