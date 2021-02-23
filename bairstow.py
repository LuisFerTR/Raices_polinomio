# Programa que calcula las raíces (reales o complejas)
# de un polinomio por medio del método de Bairstow

import math
import cmath

def formula_cuadratica_bairstow(r, s):
    """
    Función para hallar las raíces de un polinomio 
    de grado 2
    """
    raices = []

    discriminante = r*r + 4*s

    if discriminante == 0: # solo tiene una raíz
        raices.append(r/2.0)
    elif discriminante > 0: # raíces reales
        raices.append((r + math.sqrt(discriminante))/2.0)
        raices.append((r - math.sqrt(discriminante))/2.0)
    else: # raíces imaginarias
        raices.append((r + cmath.sqrt(discriminante))/2.0)
        raices.append((r - cmath.sqrt(discriminante))/2.0)

    return raices

def formula_cuadratica2(a, b, c):
    raices = []

    discriminante = b*b - 4.0*a*c

    if discriminante == 0: # solo tiene una raíz
        raices.append(-b/2.0)
    elif discriminante > 0: # raíces reales
        raices.append((-b + math.sqrt(discriminante))/(2.0*a))
        raices.append((-b - math.sqrt(discriminante))/(2.0*a))
    else: # raíces imaginarias
        raices.append((-b + cmath.sqrt(discriminante))/(2.0*a))
        raices.append((-b - cmath.sqrt(discriminante))/(2.0*a))

    return raices

def generar_b(a, r, s):
    n = len(a) - 1
    b = [None]*len(a)
    b[n] = a[n]
    b[n-1] = a[n-1] + r*b[n]
    for i in reversed(range(0, n-1)):
        b[i] = a[i] + r*b[i+1] + s*b[i+2]

    return b

def generar_c(b, r, s):
    n = len(b) - 1
    c = [None]*len(b)
    c[n] = b[n]
    c[n-1] = b[n-1] + r*c[n]
    for i in reversed(range(1, n-1)):
        c[i] = b[i] + r*c[i+1] + s*c[i+2]

    return c


def bairstow(a, r, s, tolerancia):
    """
    a: Lista de coeficientes del polinomio
    r y s: Aproximaciones iniciales
    tolerancia: Tolerancia de error
    """
    grado = len(a) - 1
    num_iter = 0 # Observar cuantas iteraciones hace
    max_iteraciones = 100
    raices = []
    b = []

    while grado > 0:
        num_iter = 0
        r_error = 100
        s_error = 100

        if grado == 1:
            raiz = -float(a[0])/float(a[1])
            raiz = raiz if raiz != -0 else 0
            raices.append(raiz)
            grado -= 1

        elif grado == 2:
            raices.extend(formula_cuadratica2(a[2], a[1], a[0]))
            grado -= 2

        else:
            while (r_error > tolerancia or s_error > tolerancia) and num_iter < max_iteraciones:
                b = generar_b(a, r, s)
                c = generar_c(b, r, s) 

                # Solución del sistema por regla de cramer
                determinante = c[2]*c[2] - c[3]*c[1]

                if determinante != 0:
                    dr = (-b[1]*c[2] + c[3]*b[0])/determinante
                    ds = (-b[0]*c[2] + c[1]*b[1])/determinante

                    r += dr
                    s += ds

                    # Errores relativos de r y s
                    if r != 0:
                        r_error = abs(dr/r)*100
                    
                    if s != 0:
                        s_error = abs(ds/s)*100

                    num_iter += 1
                else: 
                    r += 1
                    s += 1
                    num_iter = 0
            
            a = b[2:]
            grado -= 2
            raices.extend(formula_cuadratica_bairstow(r, s))

    return raices


def main():
    print(bairstow([0, 0, 2, 1], 0, 0, 1))

if __name__ == "__main__":
    main()