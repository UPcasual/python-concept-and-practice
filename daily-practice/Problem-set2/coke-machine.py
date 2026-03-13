'''
Suppose that a machine sells bottles of Coca-Cola (Coke) for 50 cents and only accepts coins in these denominations: 25 cents, 10 cents, and 5 cents.

In a file called coke.py, implement a program that prompts the user to insert a coin, one at a time, each time informing the user of the amount due. 
Once the user has inputted at least 50 cents, output how many cents in change the user is owed. Assume that the user will only input integers, 
and ignore any integer that isn’t an accepted denomination.

'''
deuda = 50
def deuda1(dinero):
    global deuda
    deuda = deuda - dinero
    print("falta ingresar esta cantidad", deuda)
    return deuda # funcion lista

def valido(dinero):
    permitido=[5,10,25]
    for i in permitido: # esta forma tambien es valida para comprobar el valor en la lista 
        if dinero == i:
            return i
    else:
        print("ingresa una moneda valida")
#    if dinero in permitido:  esta formas son valida cada uno de los items en la lista para comprobar que esten 



def main():
    while deuda >0:
        dinero = int(input("ingresa una moneda"))
        resultado_vali = valido(dinero)

        if dinero != resultado_vali:
            print("esta moneda no es valida")
        else:
            deuda1(dinero)
    print("el valor esta completo")

main()

#terminado
