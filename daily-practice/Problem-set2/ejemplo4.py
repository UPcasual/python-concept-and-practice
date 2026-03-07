def main():
    number= get_number() # se crea una funcion para optener un numero con el que trabajar 
    meow(number)

def get_number(): # esta es la funcion donde se va a preguntar por el numero 
    while True:
        n = int(input("cual es el numero"))
        if n > 0:
            break # aqui si el numero es mayor a cero se termina el bucle while 
    return n #aqui esta devolviendo el valor de n que se entrego 

# esta ultima funcion no entiendo para que la crea  eso agarra el numero que se le da y lo entrega a una funcion que lo recive luego esta 
# funcion es llamada en main donde se le coloca el valor que se consigui en number atravez de get_number
def meow(n):
    for _ in range(n):
        print("meow")