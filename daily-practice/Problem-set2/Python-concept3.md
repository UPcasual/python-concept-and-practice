# python concept 3
concepto a ver
- while
- for
- list
- validadando input 

## while
reitera una expresion, atravez de que una condicional sea verdadera o falsa
### ejemplo
    i = 3
    while i != 0 :
        print("meow")  # esto es una secuencia infinita por que no existe el momento donde se termina la seccuencia 
        i = i-1 # aqui se termina la suencia ya que cada vez que ejecuta el print reduce 1 a la variable i

## for 
si quieres una variable como i una variable numerica y ya sabes cuantas veces quieres que se ejecute, 
## list
contiene multiples variables en un una sola variable que se crea es una lista basicamente, que mas quiere que te explique 

### ejemplo2
for i in [0,1,2]:
    print("meow") # aqui va a ejecutar mew hasta que pase por cada uno de las variables en la lista

#### consejo 
en vez de utilizar una lista y una cantidad de valores en la lista puedes usar la funcion llamada range(numero), o tambien puedes no utilizar ninguna variable y solo utilizar una _ para realizar el ciclo for 
##### ejemplo del consejo 
for _ in range(3)
    print(_)

## validando el input 
para realizar esto podemos realizar un ciclo de while que se mantenga mientras sea verdadero 

### ejemplo 3 
while True:
    n= int(input(" que numero es N))
        if n > 0:
            break #aqui solo si se cumple el if se termina el ciclo 

for _ in range(n) #esta linea se ejecuta luego de que se termina el ciclo anterior y luego utiliza la variable n que se pregunto al inicio
    print("mew")

### ejemplo 4 
  
 esta  vez realizando la logica atravez de la creacion de funciones 

 def main():
    number= get_numbre() # se crea una funcion para optener un numero con el que trabajar 
    meow(number)

def get_number(): # esta es la funcion donde se va a preguntar por el numero 
    while True:
        n = int(input("cual es el numero"))
            if n > 0:
                break # aqui si el numero es mayor a cero se termina el bucle while 
    return n #aqui esta devolviendo el valor de n que se entrego 

def meow(n): # esta ultima funcion no entiendo para que la crea  eso agarra el numero que se le da y lo entrega a una funcion que lo recive
             # luego esta funcion es llamada en main donde se le coloca el valor que se consigui en number atravez de get_number 