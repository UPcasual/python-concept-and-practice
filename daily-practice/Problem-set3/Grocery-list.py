'''
Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called grocery.py, implement a program that prompts the user for items, one per line, until the user inputs control-d
(which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item,
prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.
'''

lista = {} # para agregar valor y una cantidad se debe utilziar un diccionarios.


#def orden():
    #la lista debe ser ordenado y se le debe agregar un valor de veces que se escribre
try:
    while True:
        input_ =input(("ingresas un item"))
        upper_input = input_.upper()
        if upper_input not in lista:
            lista[upper_input]= 1
        elif upper_input  in lista:
            lista[upper_input] += 1

except EOFError:
    lista_ordenada= sorted(lista)
    for item in lista_ordenada:
        print(lista[item], item)
