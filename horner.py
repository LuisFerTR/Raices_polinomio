# coding: utf8
# Programa que lee un coeficientes de grado grado y lo evalúa en un valor x
"""Declaración de la función.
Con esto damos a conocer la función al compilador. Desde este momento se puede mandar llamar"""
def horner(grado, coeficientes, x):
    """
    grado: Grado del polinomio. \n
    coeficientes: Lista de los coeficientes del polinomio, 
    comenzando por el término independiente. \n
    x: Valor a evaluar en el polinomio. 
    """
    
    polinomio = coeficientes[grado]
    k = grado - 1
    while (k >= 0):
        polinomio = coeficientes[k] + (polinomio*x)
        k = k - 1
	# Al término de este ciclo WHILE, la variable polinomio tiene el valor del P(x)
    return polinomio

""" 
# Zona de pruebas
def main():
    print(horner(3, [1, 2, 3, 1], 2.5))


if __name__ == "__main__":
    main()
 """
