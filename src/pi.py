#!/usr/bin/env python

#funcion que evalua la funcion que se va a 'integrar'
def fraccion_cuadratica(x):
    return 1 / (1+x**2)

#funcion que  dara el valor aprox. de la integral
def SumaRiemann(inicial, final, nrect, base, func):
    suma = 0.0
    punto_medio  = (inicial + base)/2 #esto dara el valor en x del punto medio del primer rectangulo

    for r in range(nrect):
        suma += func(punto_medio) * base #va a sumar el area de cada rectangulo de la iteracion
        punto_medio += base #esto pasara al siguiente punto medio
    return suma

inicial = 0
final= 1
num_rect = 100000
base = (final - inicial)/num_rect #ancho de los rectangulos

valor_integral = SumaRiemann(inicial, final, num_rect, base, fraccion_cuadratica)
pi_aprox = 4*valor_integral

print(pi_aprox)
