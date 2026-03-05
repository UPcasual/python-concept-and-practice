'''
In deep.py, implement a program that prompts the user for the answer to the Great Question of Life, the Universe and Everything, outputting Yes if the user inputs 42 or 
(case-insensitively) forty-two or forty two. Otherwise output No.
'''

print("What is the answer to the Great Question of Life, the Universe and Everything")
texto= str(input(""))
texto_modificado = str.lower(texto)
if texto_modificado == "42":
    print("si")
elif texto_modificado == "forty-two":
    print("si")
elif texto_modificado == "forty two":
    print("si")
elif texto_modificado == "cuarenta y dos":
    print("si")
elif texto_modificado == "cuarentaydos":
    print("si")
else:
    print("no")

## terminado