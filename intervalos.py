# coding: utf8
# Programa que dado un polinomio y sus raíces 
# evalúa el polinomio en intervalos y almacena
# el signo del polinomio en ese intervalo, re-
# gresa un diccionario con los intervalos de 
# signo negativo y positivo

from horner import horner
from math import inf
from random import random, uniform

def intervalos(coeficientes, raices, cifras_significativas):
    """
    coeficientes: Lista de los coeficientes del polinomio, 
    comenzando por el término independiente. \n
    raices: Lista de raíces del polinomio, pueden ser 
    reales o complejas. \n
    cifras_significativas: Cifras significativas de las 
    raíces
    """

    resultados = {"negativo": [], "positivo": []}
    grado = len(coeficientes) - 1 

    #Eliminar las raíces complejas de la lista raices y ordernarla
    raices = [x for x in raices if type(x) is not complex]
    raices.sort()

    # Para la primera raíz
    valor_prueba = raices[0] - random()
    if (horner(grado, coeficientes, valor_prueba) < 0):
        resultados["negativo"].append((-inf, raices[0]))
    else:
        resultados["positivo"].append((-inf, raices[0]))

    # Cualquier otra raíz
    for i in range(0, len(raices)-1):
        valor_prueba = round(uniform(raices[i], raices[i+1]), cifras_significativas)
        if (horner(grado, coeficientes, valor_prueba) < 0):
            resultados["negativo"].append((raices[i], raices[i+1]))
        else:
            resultados["positivo"].append((raices[i], raices[i+1]))

    # Para la última raíz
    valor_prueba = raices[len(raices)-1] + random()
    if (horner(grado, coeficientes, valor_prueba) < 0):
        resultados["negativo"].append((raices[len(raices)-1], inf))
    else:
        resultados["positivo"].append((raices[len(raices)-1], inf))

    return resultados


def main():
    print(intervalos([4, 6], [-2/3], 4))

if __name__ == "__main__":
    main()

