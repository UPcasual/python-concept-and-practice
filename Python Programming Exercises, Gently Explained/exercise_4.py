 #area(10, 4)  →  40
 #perimeter(10, 4)  →  28
 #volume(10, 4, 5)  →  200
 #surfaceArea(10, 4, 5)  →  220

 #funtion area() and perimeter() tienen length and heidth parametros

def area(length, heidth):
    area = length *heidth
    return area
def perimeter(length, heidth):
    perimetro = 2*length + 2*heidth

    return perimetro

def volume(length, heidth,width):
    volumen= length*heidth*width
    return volumen

def surfaceArea(length, heidth,width):
    surfaceArea = (length*width*2)+(length*heidth*2)+(heidth*width*2)

    return surfaceArea


assert area(10, 10) == 100

assert area(0, 9999) == 0

assert area(5, 8) == 40

assert perimeter(10, 10) == 40

assert perimeter(0, 9999) == 19998

assert perimeter(5, 8) == 26

assert volume(10, 10, 10) == 1000

assert volume(9999, 0, 9999) == 0

assert volume(5, 8, 10) == 400

assert surfaceArea(10, 10, 10) == 600

assert surfaceArea(9999, 0, 9999) == 199960002

assert surfaceArea(5, 8, 10) == 340
