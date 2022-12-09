from saludos import *

saludar()

class Saludo():
    def __init__(self):
        print("Hola, te estoy saludando desde el __init__ " \
                "de la clase Saludo")

from saludos import Saludo

s = Saludo()
