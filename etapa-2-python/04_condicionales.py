# ==========================
# Sesión 4: Condicionales
# ==========================

# # ----------------------------------------------------------------------------------------------
# Ejercicio 1
# # ----------------------------------------------------------------------------------------------

# Bloque A
precio = 280
if precio > 300:
    print("Premium")
print("Fin A")
# predicción: Fin A

# Bloque B
existencias = 0
if existencias:
    print("Hay ejemplares")
else:
    print("Sin ejemplares")
# predicción: Sin ejemplares

# Bloque C
ventas = 12
if ventas > 5:
    print("Más de 5")
if ventas > 10:
    print("Más de 10")
# predicción: Error? (Doble if / No else)
# correción: Imprime las dos condiciones.

# Bloque D
ventas = 12
if ventas > 5:
    print("Más de 5")
elif ventas > 10:
    print("Más de 10")
# predicción: Más de 5

# ----------------------------------------------------------------------------------------------
Ejercicio 2
# ----------------------------------------------------------------------------------------------

# Pruébalo con 25, 5 y 0. Encuentra el error y corrígelo sin cambiar
# ninguna condición, solo su orden.

ventas_mes = 5

if ventas_mes > 0:
    rotacion = "Baja"
elif ventas_mes > 20:
    rotacion = "Media"
elif ventas_mes > 40:
    rotacion = "Alta"
else:
    rotacion = "Sin ventas"

print(f"Rotación: {rotacion}")

# Respuesta: Las condiciones estan al revés, todos los números que sean superiores a 0 van a tomar
# siempre "Baja", al ser la primera que se cumple, no considera el resto de condiciones.

if ventas_mes > 40:
    rotacion = "Alta"
elif ventas_mes > 20:
    rotacion = "Media"
elif ventas_mes > 0:
    rotacion = "Baja"
else:
    rotacion = "Sin ventas"

print(f"Rotación: {rotacion}")

# ----------------------------------------------------------------------------------------------
# Ejercicio 3
# ----------------------------------------------------------------------------------------------

existencias = 3
if existencias < 5
    print("Bajo")

# R: Le falta ":" al final del if
    
existencias = 3
if existencias < 5:
print("Bajo")

# R: el print no tiene la identación correcta para unirse al if, son bloques separados

existencias = 3
if existencias = 0:
    print("Agotado")
    
# R: Usa incorrectamente el signo "=" para referir a "Igual a", en su lugar es "=="
    
# ----------------------------------------------------------------------------------------------
# Ejercicio 4: Con una variable existencias, imprime Agotado si 
# es 0, Bajo si es menor que 5 o Suficiente en cualquier otro caso. Prueba con 0, 3, 5 y 20.
# ----------------------------------------------------------------------------------------------

existencias_4 = 20

if existencias_4 == 0:
    print("Agotado")
elif existencias_4 < 5:
    print("Bajo")
else:
    print("Suficiente")

# ----------------------------------------------------------------------------------------------
# Ejercicio 5: Un cliente compra una cierta cantidad de un libro obtiene descuento. 
# De 1 a 4 es 0%, 5 a 9 es 5%, 10 a 19 es 10%, 20 o más es 15%. Si la cantidad es
# negativa, imprime "Cantidad Inválida". Si es válida imprime el ticket: subtotal,
# porcentaje aplicado, monto del descuento, y el total, a 2 decimales.
# ----------------------------------------------------------------------------------------------

# Pseudocódigo:
# 1. Datos: cantidad vendida y precio unitario
# 2. Si la cantidad es cero o negativa -> "Cantidad Invalidad"
# 3. Si no:
#   3.1 Decisión de descuento:
#       - 20 o más: 15%
#       - 10 o más: 10%
#       - 5 o más: 5%
#       - Menor a 5: 0%
# 4. Subtotal: cantidad vendida * precio unitario
# 5. Monto de descuento: Subtotal * Descuento
# 6. Total: Subtotal - Monto de descuento
# 7. Impresión del ticket

cantidad_vendida = int(input("Cantidad de libros: "))
precio_unitario = float(input("Precio de cada libro: "))

if cantidad_vendida <= 0:
    print("Cantidad Inválida")
else:
    if cantidad_vendida >= 20:
        descuento = 0.15
    elif cantidad_vendida < 5:
        descuento = 0
    elif cantidad_vendida < 10:
        descuento = 0.05
    else:
        descuento = 0.10
        
    subtotal = cantidad_vendida * precio_unitario
    monto_descuento = subtotal * descuento
    total = subtotal - monto_descuento

    print(f"Subtotal:               ${subtotal:.2f}")
    print(f"Descuento aplicado:     {descuento * 100:.0f}%")
    print(f"Monto de descuento:     ${monto_descuento:.2f}")
    print(f"Ticket total:           ${total:.2f}")

# ----------------------------------------------------------------------------------------------
# Ejercicio 6: Reescribe el validador de la sesión 3, pero ahora, en lugar de 
# solo True o False, que diga por qué un ISBN no es válido:
# Longitud incorrecta: tiene N caracteres
# Contiene caracteres que no son dígitos
# Prefijo inválido: X
# ISBN válido
# ----------------------------------------------------------------------------------------------

# Pseudocódigo:
# 1. Ingresar ISBN
# 2. Verificar si la longitud NO es correcta, y notificar longitud ingresada.
# 3. Verificar si no todos son dígitos y notificar que existen carácteres inválidos.
# 4. Verificar si el prefijo no es "978" o "979" y notificar que el prefijo que contiene.
# 5. Si ninguna se cumple, notificar ISBN es válido

# isbn = "9786071612345"
# isbn = "978607161234"
# isbn = "97860716123X5"
isbn = "1234567890123"
prefijo = isbn[0:3]

if len(isbn) != 13:
    print(f"Longitud incorrecta, tienen {len(isbn)} carácteres")
elif not isbn.isdigit():
    print(f"{isbn} contiene carácteres que no son dígitos")
elif prefijo != "978" and prefijo != "979":
    print(f"{isbn} usa el prefijo {prefijo} inválido")
else:
    print(f"ISBN Válido: {isbn}")
    
# Resultado 1: ISBN Válido 9786071612345
# Resultado 2: Longitud incorrecta, tienen 12 carácteres
# Resultado 3: 97860716123X5 contiene carácteres que no son dígitos
# Resultado 4: 1234567890123 usa el prefijo 123 inválido

# ¿Porqué en ese orden?
# La longitud es la condición más importante, de nada sirve buscar digitos o
# prefijos si no tiene los carácteres correctos, enseguida los dígitos por la misma
# lógica en que seleccionamos la longitud primero.