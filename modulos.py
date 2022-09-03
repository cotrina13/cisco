""""import module as alias =import math as m
*tambien se le pude colocar alias funciones o variables del modulo
from math import pi as PI, sin as sine
*se le puede colocar un alias al momento de importar
un modulo
*tambien se puede importar todo un modulo así import modulo *
*Se pueden importar varios modulos así:
import modulo1,modulo2
"""


import math
print(math.sin(math.pi/2 ))
def sin(x):
    if 2 * x == pi:
        return 0.99999999
    else:
        return None


pi = 3.14
#con la funcion dir se puede ver todas las entidades dentro del
#modulo
print(sin(pi/2))
print(math.sin(math.pi/2))
for name in dir(math):
    print(name, end="\t")