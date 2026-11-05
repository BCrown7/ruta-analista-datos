# ====================================
# LÓGICA DE PROGRAMACIÓN
# ====================================

# Sesión 1: entorno y ejecución de código

print("Hola, Python")
2 + 3

print("Pedro", "Páramo")  # Predicción: Pedro Páramo
print("Pedro" + "Páramo")  # Predicción: PedroPáramo
print("2" + "3")  # Predicción: 23
print(2 + 3)  # Predicción: 5
print("ja" * 3)  # Predicción: jajaja
print("A", "B", "C", sep="-")  # Predicción: A-B-C
print("Uno", end=" | ")  # Predicción: Uno |
print("Dos")  # Predicción: Dos

# Prueba de errores

# print("Total de libros"       # SyntaxError: paréntestis sin cerrar
# prin("Inventario")            # NameError: print mal escrito
# print("Total: " + 3)          # TypeError: no se puede sumar a una cadena

# Ejercicio

# Paso 1: Imprimir una ficha de libro en cuatro líneas
print("Titulo")
print("Autor")
print("Editorial")
print(1997)

# Paso 2: Imprimir el mismo texto con datos separados por " | "

print("Título", "Autor", "Editorial", 1997, sep=" | ")

# Paso 3: Reto de lógica en código:

print("Ventas:", 10 + 5)
# Predicción: Ventas: 15
# El uso de "," en un print crea un espacio, imprime la cadena, y ademas realiza
# la operación en el segundo argumento del print.

print("Ventas: " + "10" + "5")
# Predicción: Ventas: 105
# Los números están envueltos en "", lo que los convierte en cadenas de texto, el
# "+" une dos cadenas de texto como uniriía una "A" con una "B".

print("10" * 2, 10 * 2)
# Predicción: 1010 20
# Las cadenas de texto se pueden multiplicar, duplica el texto "10" dos veces, mientras que
# en el segundo argumento, trata dos valores numéricos y resuelve la operación.

print("Fin", end="")
print("!")
# Predicción: Fin!
# El uso de end elimina el salto de linea del primer print
# y unifica los dos prints en una única línea.
