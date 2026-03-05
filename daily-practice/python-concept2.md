# Condicionales 


## inventar funciones
es importante entender que siempre es una buena estrategia crear una funcion para desarrollar el problema, asume diferentes resultados, solo asume que existira una forma de resolverlo a travez de las funciones que tal vez aun no creas 

### ejemplo 
def main():
    x = int(input("what x"))
    if is_even(x): #la funcion que aun no existe
        print("even)
    else:
        print("odd")

def is_even(n)
    if n % 2 == 0:
        return True
    else:
        return False

main()