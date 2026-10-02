#
#find and replace
#
#findAndReplace('The fox', 'fox', 'dog')  →  'The dog'
#
# escribe una funcion findAndreplace() con 3 parametros: text es el string con texto para replazar, oldText es el texto para ser remplazado y newText es el texto de remplazo, toma en cuenta que la funcion debe ser case sensitive
#
#
#
#
#

def findAndReplace(text,oldText,newText):
    replazo=""
    i = 0
    while i < len(text):
        if text[i:i+len(oldtext)] == oldText:
            replazo+=newText
        else:
            text+=text[i]
            i+=1

            return replazo

assert findAndReplace('The fox', 'fox', 'dog') == 'The dog'

assert findAndReplace('fox', 'fox', 'dog') == 'dog'

assert findAndReplace('Firefox', 'fox', 'dog') == 'Firedog'

assert findAndReplace('foxfox', 'fox', 'dog') == 'dogdog'

assert findAndReplace('The Fox and fox.', 'fox', 'dog') == 'The Fox and dog.'
