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

#ejemplo de como asignar scopes a namespaces
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)
    do_nonlocal()
    print("After nonlocal assignment:", spam)
    do_global()
    print("After global assignment:", spam)

scope_test()
print("In global scope:", spam)

#ejemplo de clases
class MyClass:
    """A simple example class""" 
    #esta es una documentacion de la clase que se puede pedir con __doc__
    i = 12345 #si se pone asi suenta dentro de la clase, es una variable de clase, sino va en el init puesto en el self

    # __init__ es el metodo que se enjecuta en el inicio, siempre le llega un self como parametro de inicio
    def __init__(self):
        self.i = self.i+1

    def f(self):
        return 'hello world'

#si uno lo deja así, los atributos y metodos son publicos
#para crear una instancia, solo se llama como si fuese un metodo

x = MyClass()

print(MyClass.i)
print(x.i)

#parece que se pueden hacer cosas locas como estas que es definir una variabnle en el momento dento de un objeto y luego eliminarla
x.counter = 1
while x.counter < 10:
    x.counter = x.counter * 2
print(x.counter)
del x.counter
# print(x.counter) si dejo esto tira un error que dice que no existe la variable .. :)

print(x.f()) #llama a un metodo
#se puede hacer un lambda con el metodo así:

funcionF = x.f
print(funcionF())

#hay una forma muy cool de llamar a una función de un objeto que es llama a la clase y pasarle el objeto como parametro, que luego recibirá en la variable self

MyClass.f(x)
# es lo mismo que llamar a x.f()

#atributo de clase y de instancia, la instancia va en el self
class Dog:
    kind = 'canine'         # class variable shared by all instances
    def __init__(self, name):
        self.name = name    # instance variable unique to each instance

#si quiero que los trucos sean diferente por perro los tengo que poner como variable de instancia obvio
class Dog2:
    def __init__(self, name):
        self.name = name
        self.tricks = []    # creates a new empty list for each dog
    def add_trick(self, trick):
        self.tricks.append(trick)
    def _dormir(self):
        pass
        #no hay atributos ni funciones privadas, solo por convenio si empieza con underscore sabes que es privado y puede cambiar

perro = Dog("fiby")

print(perro.__class__)

class Cachorro(Dog):
    def truco(self):
        print("wow "+self.name)

c = Cachorro("pip")
c.truco()

print(isinstance(c,Cachorro))
print(issubclass(Cachorro,Dog))

#truco para usar una clase como una estructura, dado que se le pueden crear directamente las variabels desde afuera
class Employee:
    pass

john = Employee()  # Create an empty employee record
# Fill the fields of the record
john.name = 'John Doe'
john.dept = 'computer lab'
john.salary = 1000

print(str(john))

#ejemplo de como crear un iterador a mano:
class Reverse:
    """Iterator for looping over a sequence backwards."""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    #hay que definir un metodo __iter__
    def __iter__(self):
        #el cual devualva un objeto que implemente __next__, se devueve este mismo
        return self

    def __next__(self):
        if self.index == 0:
            #si queremos indicar que terminó, se lanza esta exception
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

rev = Reverse('spam')
for char in rev:
    print(char)



# The yield statement suspends function’s execution and sends a value back to caller, 
# but retains enough state to enable function to resume where it is left off. When resumed, 
# the function continues execution immediately after the last yield run. This allows its code to 
# produce a series of values over time, rather them computing them at once and sending them back like a list.
# The yield statement suspends function’s execution and sends a value back to caller, but retains 
# enough state to enable function to resume where it is left off. When resumed, the function 
# continues execution immediately after the last yield run. This allows its code to produce a 
# series of values over time, rather them computing them at once and sending them back like a list.

# A Simple Python program to demonstrate working 
# of yield 
  
# A generator function that yields 1 for first time, 
# 2 second time and 3 third time 
def simpleGeneratorFun(): 
    yield 1
    yield 2
    yield 3
  
# Driver code to check above generator function 
for value in simpleGeneratorFun():  
    print(value)

import json

# some JSON:
x =  '{ "name":"John", "age":30, "city":"New York"}'

# parse x:
y = json.loads(x)

# the result is a Python dictionary:
print(y["age"])

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x,indent=4))


#como se hace un get de internet
import urllib.request, json 

with urllib.request.urlopen("http://maps.googleapis.com/maps/api/geocode/json?address=google") as url:
    data = json.loads(url.read().decode())
    print(data)

import json,urllib.request
data = urllib.request.urlopen("https://api.github.com/users?since=100").read()
output = json.loads(data)
print ("login: " + output[0]["login"])