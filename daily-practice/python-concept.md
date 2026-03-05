## concepto 1 
una de las cosas que mas se destacan de esta clase 0 es el concepto de definir funciones
la funcion definir nuevas funciones se realiza con def

un ejemplo clasico es el de 
def hello():
....(todo lo escrito aqui esta dentro de la funcion hello)
### ejemplo
def hello(tu)
    print("hello,", tu)

name = input("what your name)
print("holla como estas" )
hello(name)  ## aqui se esta llamando la funcion hello y de forma adicional se le esta entregando el valor de la variable name que contiene el nombre integrado por el usuario
el resultado de esto es 
what your name : [ingresa el nombre]
holla como estas 
hello, [nombre ingresado] 

## Concepto 2
el segundo concepto que considero que fue el mas relevante es el de Return
esto es para que mas de una funcion creada pueda entregar el valor que se cree

### ejemplo 3
def main():
    x = int(input(whats x))
    print("x squeared is " , squeare(x))
    ## en este caso el problema de esta funcion es que la funcion squeare(x)
    no esta definida
    #vamos a definir squeare creado la funcion squeared
def squared(n)
    return n * n
