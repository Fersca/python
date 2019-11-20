msg = "hello world"
print(msg.capitalize())

# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = '# Meter single quote es lo mismo que double, ambos sirven para strings'

tamanio = len(text)


listas = [1,2,3,4,5]
listas[3] = 10
print(listas)

if len(listas)<5:
    print("menor a 5")
elif len(listas)<10:
    print("menor a 10")    
else:
    print("otra cosa")

# el for no es como en C, itera sobre un slice o string

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# se puede usar range para iterar en una secuencia de numeros

for i in range(5):
    print("numero: ", i)

# para iterar sobre los índices de una secuencia, está bueno este truco:

for i in range(len(words)):
    print("pos:",i," palabra: ",words[i])

# se puede usar el brack como en C, pero se pouede poner un else en for y while, 
# que se ejecuta si no hubo break (o sea, llegó el final)

for i in range(75):
    if i<50:
        continue
    if i>60:
        pass
    if i==76:
        break
else:
    print("no hay numero 76")

# funciones.... se crean con "def" se les puede poner un texto debajo el cual es el comentario del a funcion
# devuelven siemopre un valor, si no ponemos return, devulve "None"

def pares(n, palabra="hola"):
    "Devuelve los numeros pares entre 1 y N"
    if palabra in "fer": #in se puede usar para chequear por palabras
        print("Easter Egg!")
    result = []
    for i in range(n):
        if i%2==0:
            result.append(i)
    return result

print("Pares: ", pares(20,"fer"))

#cuando se llama con parámetros se puede pasar de forma desempackada si lo tenemos en una lista de slice
argumentos = [3,6]
for i in range(*argumentos):
    print("numero", i)

# se pueden crear funciones lambda
def incremento(n):
    return lambda x: x+n

f=incremento(10)
print(f(33))

#documentación: por convención, se pone una linea de summary y luego de dos lineas en blanco el detalle.

def documentacion():
    """Pequeña documentación

    Este es el detalle de la documentación"""
    pass

print(documentacion.__doc__)

# listas, tuplas, sets and dictionaries
lista2 = [1,2,3,4,5]
lista2.append(8)

tupla = "fer",3,["hola","chau"]
print(len(tupla))
sett = {1,2,3,4,5,6,6,6,6} ##unsorted and no duplicate
print(sett)

#asi se importa un modulo, es el nmombre del archivo
import fibo
fibo.fib(1000)
fib = fibo.fib
fib(1000)

from fibo import fib2
print(fib2(1000))

print(__name__)

import sys
print(sys.path)

dir(fibo)
dir(sys)

#formatting, esta forma está piola
anio = 2018
evento = "Mundial"
print(f"el {evento} fue el mejor evento del {anio}")

#la función str() y repr() sirven para convertir variables a representaciones de string, pero repr() es mas para representaciones de computadora
print(str(1/7))
print(repr(1/7))

#abrir archivos, open devuelve un objeto File.
#f = open('workfile', 'w') #primer argumento es el nobre del file, el segundo la acción, w, r, a (write, read, append), r+ 
#es para lectura escritura y si no se especifica nada el default es read
#los files se abren en modo texto, o sea, se encodean en testo, pero si al modo de apertura se le anexa una b, quiere decir que es binario

#se puede usar con with, que sirve para hacer una especie de bloque try catch.

with open("workfile.txt", 'r') as f:
    read_data = f.read()

f.close()
print(read_data)




