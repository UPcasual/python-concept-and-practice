# python concept 3
concepto a ver
- while
- for
- list
- validadando input 
- len
- dict
- nested loops



## while
reitera una expresion, atravez de que una condicional sea verdadera o falsa
### ejemplo
    i = 3
    while i != 0 :
        print("meow")  # esto es una secuencia infinita por que no existe el momento donde se termina la seccuencia 
        i = i-1 # aqui se termina la suencia ya que cada vez que ejecuta el print reduce 1 a la variable i

## for 
si quieres una variable como i una variable numerica y ya sabes cuantas veces quieres que se ejecute, 
## list []
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

## iterar en las listas 
una lista es un set de varias variables 
una variable puede almacenar una lista 
students = ["clara","pablo","ron"]

para llamar el contenido dentro de una lista se llama la variable y la posicion de la variable que quiero 
print(students[0]) esto llamara a clara 

la utilizacion para for en las listas para desplegar todas la lista en la variable 

for students in students # 
    print(students) # esto va a imprimir la lista la cantidad que existe en la lista 

## len 
esta funcion de python va a ver la cantidad que tiene una lista
students = ["clara","pablo","ron"]
print(len(students)) # lo que va a entregar es la cantidad de 3 ya que esta es lo que tiene 

aplicando len en la lista para que asi la lista se itete atravez de la posicion de la lista y no la variable dentro de la lista 
for i in range(len(students)) # esto utiliza range que solo recibe valores numericos, asi que se utiliza la funcion len para poder la cantidad de varibales    dentro                          #de la lista
for in in range(len(students)):
    print(student[i])# esto va imprimir el numero de la lista i no va tomar la identidad de lo que esta dentro de la lista

## dict {}
permite asociar una variable con otra o keys and values, los diccionarios te permite llamar la variable por la nombre a diferencia de la lista que esta en un listado de posicion numerico
students = {} # esto es un diccionario vacio

cuando utilizas una funcion for en un diccionario este itera en todas las keys 
como en el ejemplo6
### ejemplo 5 
    students = {"clara":"norte",
                "juan":"sur",
                "pedro": "este"
                ""sofia":"oeste"}

    print(students["hermione])

### ejemplo6 

    students = {"clara":"norte",
                "juan":"sur",
                "pedro": "este"
                ""sofia":"oeste"}

    for student in students 
        print(student) # aqui estamos llamando a  estudiante que esta en el dic de estudiantes esto esta muy relacionado con la key y con el value 

    for student in students 
        print(student,students[i]) # aqui estamos llamando a lo

    for student in students 
        print(student,students[student]) llamamos el valor y despues llamamos la llave del valor que esta dentro del dic students


# dic2 
que sucede si tenemos mas informacion como lo pueden ser database, una lista de diccionaciones o una coleccion de diccionarios 

### ejemeplo7

students = [                                                #aqui tenemos una lista de diccionarios 
    {"name":"clara:, "house": "derecha", "esquina":"abajo"}, # "name" es la llave, "clara" seria el valor 
    {"name":"jose:, "house": "izquierda", "esquina":"arriba"}
    {"name":"claudio:, "house": "abajo", "esquina":"None"} # none indica que no existe valor 

]

