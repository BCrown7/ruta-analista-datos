# Sesión 2: Tipos de variables

# Tipos de datos

print(type(10))         # Predicción: integer
print(type(10.0))       # Predicción: float
print(type("10"))       # Predicción: string
print(type(True))       # Predicción: boolean
print(type(10/2))       # Predicción: integer
print(int("7") + 3)     # Predicción: 10
print(int(9.99))        # Predicción: 9
print(float("3.5")*2)   # Predicción: 7
print(bool(0))          # Predicción: FALSE
print(bool("0"))        # Predicción: FALSE
print(bool(""))         # Predicción: FALSE
print(0.1+0.2)          # Predicción: 0.3

# Rastrear variables

existencias = 10
vendidos = 3
existencias = existencias - vendidos
vendidos = 5
print(existencias)      # Predicción: 7
print(vendidos)         # Predicción: 5

# Errores de tipo

# print(int("12.5"))
# Predicción: ValueError, no puede tomar un float y transformarlo a integer en una cadena.
# print(int("doce"))
# Predicción: ValueError, no puede transformar una cadena en número.
# print(existencia)
# Predicción: NameError, la variable esta mal escrita

# -------------
# Ejercicio #2
# -------------

# 2.1: Crea variables para un libro, e imprime la ficha con f-strings y su tipo.

titulo = "Libro 1"
autor = "Bryan"
isbn = "1324354657689"
precio = 346.5
existencias = 4
disponible = True

print(f"El libro {type(titulo)} {titulo}, del autor {type(autor)} {autor} con el ISBN {type(isbn)} {isbn} tiene un precio de {type(precio)} {precio} cuenta con {type(existencias)} {existencias} y se encuentra disponible {type(disponible)} {disponible}")

# 2.2 Con un precio unitario, una cantidad y un descuento del 10%, calcula el subtotal, 
# el monto del descuento y el total. Imprime el ticket con todos los montos a 2 decimales y una línea por concepto.

descuento = 0.9

print(f"Precio: {precio:.2f} \nCantidad: {existencias} \nDescuento: 10% \nSubtotal: {existencias * precio} \nTotal C/ Descuento: {(existencias * precio) * descuento}")

# CORRECCION SUGERIDA 2.2

# 1. Datos de entrada: precio unitario, cantidad vendida, tasa de descuento.
# 2. Subtotal = precio por cantidad.
# 3. Monto del descuento = subtotal por la tasa.
# 4. Total = subtotal menos el descuento.
# 5. Imprimir una línea por concepto, con 2 decimales.

precio_unitario = 350
cantidad_vendida = 2
tasa_descuento = 0.10

subtotal = precio_unitario * cantidad_vendida
monto_descuento = subtotal * tasa_descuento
total = subtotal- monto_descuento

print(f"Subtotal:   ${subtotal:.2f}")
print(f"Descuento:  ${monto_descuento:.2f}")
print(f"Total:      ${total:.2f}")

# 2.3 Pide al usuario el título, la cantidad vendida y el precio, y calcula el total

cantidad = int(input("¿Qué cantidad de libros llevarás? "))
precio = float(input("Qué precio unitario tiene? "))

print(f"El costo total por {cantidad} y precio unitario de {precio} es de ${cantidad * precio:.2f}")