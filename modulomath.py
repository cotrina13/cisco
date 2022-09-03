""""e → una constante con un valor que es una aproximación del número de Euler (e).
exp(x) → encontrar el valor de ex.
log(x) → el logaritmo natural de x.
log(x, b) → el logaritmo de x con base b.
log10(x) → el logaritmo decimal de x (más preciso que log(x, 10)).
log2(x) → el logaritmo binario de x (más preciso que log(x, 2)).
pow(x, y) → encuentra el valor de xy (toma en cuenta los dominios).
ceil(x) → devuelve el entero más pequeño mayor o igual que x.
floor(x) → el entero más grande menor o igual que x.
trunc(x) → el valor de x truncado a un entero (ten cuidado, no es equivalente a ceil o floor).
factorial(x) → devuelve x! (x tiene que ser un valor entero y no negativo).
hypot(x, y) → devuelve la longitud de la hipotenusa de un triángulo rectángulo con las 
longitudes de los catetos iguales a (x) y (y) (lo mismo que sqrt(pow(x, 2) + pow(y, 2)) pero más preciso)."""
from math import ceil, floor, trunc

x = 1.4
y = 2.6

print(floor(x), floor(y))
print(floor(-x), floor(-y))
print(ceil(x), ceil(y))
print(ceil(-x), ceil(-y))
print(trunc(x), trunc(y))
print(trunc(-x), trunc(-y))