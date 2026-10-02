#
#
# una funcion getChessSquareColor() con parametros column y row, la funcion debe
#devolver black or white dependiendo del color
#las tablas de ajedres son de 8x8 y empiezan en 0 y termina en 7
#si el argumento esta fuera del rango de la column y row, la funcion debe devolver blank string
#
# 0.0 blanca 7.0 negra and 0.7 negra y 7.7 blanca
# 0.0 blanca 0.1 negra 0.2 blanca 0.3 negra 0.4 blanca 0.5 negra 0.6 blanca 0.7 negra


def getChessSquareColor(column, row):
    if column < 0 or column > 7 or row < 0 or row > 7:
        return ''
    if column%2 == row%2:
        return 'white'
    else:
        return 'black' # complicado no lo pude hacer yo, tuve que ver el solucionario





assert getChessSquareColor(0, 0) == 'white'

assert getChessSquareColor(1, 0) == 'black'

assert getChessSquareColor(0, 1) == 'black'

assert getChessSquareColor(7, 7) == 'white'

assert getChessSquareColor(0, 8) == ''

assert getChessSquareColor(2, 9) == ''
