# Programa principal que lee un polinomio de grado n > 0 y localiza sus puntos notables.
# El programa tendrá las entradas
# Grado ->
# Coeficientes ->
# Cifras significativas ->
# y entregará como resultado
# Todas las raíces reales y complejas.
# -> Las coordenadas de los extremos locales y su tipo (máximo o mínimo).
# -> Las coordenadas de los puntos de inflexión.
# -> Los intervalos en que la función es creciente y en que es decreciente.
# -> Los intervalos en que la función es cóncava hacia arriba y en que es cóncava hacia abajo.

from horner import horner
from derivar import derivar
from intervalos import intervalos
from bairstow import bairstow
from math import inf

# Leer grado
grado = int(input("Introduce el grado del polinomio: "))

# Pedir los coeficientes del polinomio, comenzando por el término independiente
print("Introduce los coeficientes del polinomio comenzando por el término independiente\n"+
		"Coeficientes:")
coeficientes = []

for i in range(grado+1):
	coeficiente = float(input("a" + str(i) + ": "))
	coeficientes.append(coeficiente)

primera_derivada = derivar(coeficientes)
segunda_derivada = derivar(primera_derivada)

# Leer cifras significativas
cifras_significativas = int(input("Introduce la cantidad de cifras significativas: "))

# Todas las raíces reales y complejas.
raices_polinomio = [1j, -1j]  # bairstow()
raices_primera_derivada = [0] # bairstow()
raices_segunda_derivada = [0] #bairstow()

# Los intervalos en que la función es creciente y en que es decreciente.
intervalos_crecimiento = intervalos(primera_derivada, raices_primera_derivada, 
cifras_significativas)

# Las coordenadas de los extremos locales y su tipo (máximo o mínimo).
maximos = []
minimos = []

dict_positivos = dict(intervalos_crecimiento["positivo"])	

# Si -inf está en los intervalos positivos, quiere decir que el 
# que le sigue está en los negativos, entonces el primer punto
# crítico tiene una relación + -> -, por lo tanto es un máximo
# y el siguiente punto crítico es un mínimo y el siguiente un
# máximo y así sucesivamente.
if -inf in dict_positivos:
	for i in range(len(raices_primera_derivada)):
		x = raices_primera_derivada[i]
		if i % 2 == 0:
			maximos.append((x, horner(grado, coeficientes, x)))
		else:
			minimos.append((x, horner(grado, coeficientes, x)))
else: 
	for i in range(len(raices_primera_derivada)):
		x = raices_primera_derivada[i]
		if i % 2 == 0:
			minimos.append((x, horner(grado, coeficientes, x)))
		else:
			maximos.append((x, horner(grado, coeficientes, x)))

# Las coordenadas de los puntos de inflexión.
coord_inflexion = []

for x in raices_segunda_derivada:
	coord_inflexion.append((x, horner(grado, coeficientes, x)))

# Los intervalos en que la función es cóncava hacia arriba y en que es cóncava 
# hacia abajo.
intervalos_concavidad = intervalos(segunda_derivada, raices_segunda_derivada,
cifras_significativas)

# Mostrar información
print()
print("Las raíces del polinomio son:")
for x in raices_polinomio:
	print(x, end=", ")

print() 

print("Las coordenadas de los mínimos locales son:")
for x in minimos:
	print(x, end=", ")

print() 

print("Las coordenadas de los máximos locales son:")
for x in maximos:
	print(x, end=", ")

print() 

print("Los intervalos donde el polinomio decrece son:")
for x in intervalos_crecimiento["negativo"]:
	print(x, end=", ")

print() 

print("Los intervalos donde el polinomio crece son:")
for x in intervalos_crecimiento["positivo"]:
	print(x, end=", ")

print() 

print("Las coordenadas de los puntos de inflexión son:")
for x in coord_inflexion:
	print(x, end=", ")

print() 

print("Los intervalos donde el polinomio es cóncavo hacia abajo son:")
for x in intervalos_concavidad["negativo"]:
	print(x, end=", ")

print() 

print("Los intervalos donde el polinomio es cóncavo hacia arriba son:")
for x in intervalos_concavidad["positivo"]:
	print(x, end=", ")

print() 
