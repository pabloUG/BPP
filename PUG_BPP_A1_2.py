import io

txtFile = io.IOBase()

try:
    txtFile = open("fichero.txt","r")
except IOError as ioE:
    print (f"Error al abrir el fichero '{ioE.filename}' - {ioE}")
except Exception as e:
    print (e)
finally:
    try:
        txtFile.close()
    except Exception as e:
        print (f"Error {e}")
    finally:
        print("El programa se ha ejecutado completamente")