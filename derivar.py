# coding: utf8
# Métodos numéricos 15-16
# Luis Fernando Talavera Rivera
# Fecha: 24/02/2021
#
# Programa que deriva un polinomio de grado n
# Recibe de entrada una lista de n coeficientes del polinomio
# Regresa una lista con n - 1 coeficientes de la derivada del polinomio

def derivar(coeficientes):
    """
    coeficientes: Lista de los coeficientes del polinomio, 
    comenzando por el término independiente.
    """
    
    d_coeficientes = []

    # Deriva cada término y coloca el 
    # coeficiente en la lista d_coeficientes
    for i in range(1, len(coeficientes)):
        d_coeficientes.append(coeficientes[i]*i)

    return d_coeficientes

""" 
# Zona de pruebas
def main():
    print(derivar([1, 2, 0, 3]))

if __name__ == "__main__":
    main()
 """
