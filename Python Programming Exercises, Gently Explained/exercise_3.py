#determinar si un numero es par o inpar la solucion puede ser escrito en una linea ??
# este utiliza el operado % (este deja el resto de una division)

#is odd(13) es true
#is even(12) false

# el parametro es number
def isOdd(number):

    return number % 2 == 1
def isEven(number):
    return number % 2 == 0

assert isOdd(42) == False

assert isOdd(9999) == True

assert isOdd(-10) == False

assert isOdd(-11) == True

assert isOdd(3.1415) == False

assert isEven(42) == True

assert isEven(9999) == False

assert isEven(-10) == True

assert isEven(-11) == False

assert isEven(3.1415) == False
