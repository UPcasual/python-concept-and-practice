# tempeture conversion
#coverttocelsius(32) -> 0
#convertofahrenheit(100) - > 212

# description
# crear una funcion para transformar una fahrenheit que usa un parametro degreescelsius, return el fahrenheit
#despues crea una funcion llamada converttocelsius() con un parametro degreesfahrenheit y return a number of this tempeture in degrees celsius
#

def convertToCelsius(degreesFarehenheit):

    return (degreesFarehenheit - 32) * (5/9)
def convertToFahrenheit(degreesCelsius):

    return degreesCelsius * (9/5) + 32

def main():
    print("vamos a convertir algunas cosas")
    decision = input("que quieres convertir (C)elsius o (F)ahrenheit").lower()
    if decision == "c":
        temp = float(input("ingresa la temperatura en celsius: "))
        result = convertToFahrenheit(temp)
        print(f"{temp} C = {result} F")
    elif decision == "f":
        temp = input("ingresa la temperatura en fahrenheit: ")
        result = convertToCelsius(temp)
        print(f"{temp} F = {result} C")
    else:
        print("no es valida la opcion")

# assert statement para el programa si la condicion es falsa
assert convertToCelsius(0) == -17.77777777777778
assert convertToCelsius(180) == 82.22222222222223
assert convertToFahrenheit(0) == 32
assert convertToFahrenheit(100) == 212
assert convertToCelsius(convertToFahrenheit(15)) == 15
assert convertToCelsius(convertToFahrenheit(42)) == 42.00000000000001

main()
