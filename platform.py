from platform import platform
""""El módulo platform permite acceder a los datos 
de la plataforma subyacente, es decir, hardware,
sistema operativo e información sobre la versión 
del intérprete."""
print(platform())
print(platform(1))
print(platform(0, 1))

from platform import machine
""" el nombre genérico del procesador que 
ejecuta el sistema operativo junto con Python y el código"""
print(machine())
from platform import processor
"""La función processor() devuelve una cadena con el
nombre real del procesador (si lo fuese posible)."""
print(processor())
from platform import system
"""Una función llamada system() devuelve 
el nombre genérico del sistema operativo en una cadena."""
print(system())
from platform import version
"""La versión del sistema operativo se proporciona 
como una cadena por la función version()."""
print(version())
