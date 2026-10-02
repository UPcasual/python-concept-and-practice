##
## escribe una funcion que se llama writeToFile() con dos parametros, uno con el nombre y el otro con el texto dentro del archivo
## escribe una segunda funcion appendToFile() la cual es identica a writeToFile() coin la excepcion de que el archivo se abre en append mode instead of write mode
## escribe una tercera funcion que se llame readFromFile() con un parametro para el filename para abrirlo.
##estas funciones deben entregar el contenido completo del archivo como un string
##
##

def writeToFile(filename,texto):
    with open(filename,"w") as fileobj:  #"x" crea el archivo
        fileobj.write(texto)
    return
def appendToFile(filename, texto):
    with open(filename, "a") as fileobj:# "a" abre un archivo para append y tambien crea el archivo si no existe
        fileobj.write(texto)
    return
def readFromFile(filename):
    with open(filename,"r") as fileobj:
        return fileobj.read()


writeToFile('greet.txt', 'Hello!\n')

appendToFile('greet.txt', 'Goodbye!\n')

assert readFromFile('greet.txt') == 'Hello!\nGoodbye!\n'
