# Sesión 3: Operadores

# =====================================================================================

# Ejercicio 1

print(25 // 6)                      # Predicción: 4
print(25 % 6)                       # Predicción: 1
print(10 % 2)                       # Predicción: 0
print(2 + 3 * 4)                    # Predicción: 14
print((2 + 3) *4)                   # Predicción: 20
print(7 == 7.0)                     # Predicción: False     # Corrección: True
print("7" == 7)                     # Predicción: False
print("Zapata" < "arreola")         # Predicción: True
print(True and False)               # Predicción: True      # Corrección: False
print(True or False)                # Predicción: True
print(not True)                     # Predicción: False
print(True or False and False)      # Predicción: True
print((True or False) and False)    # Predicción: True      # Corrección: False
print("Rulfo" in "Juan Rulfo")      # Predicción: True
print("rulfo" in "Juan Rulfo")      # Predicción: False

existencias = 10
existencias -= 4
existencias *= 2
print(existencias)                  # Predicción: 12

# =====================================================================================

# Ejercicio 2

cantidad = 0
total = 500

# Código con error intencional
# print(total / cantidad > 100 and cantidad != 0)
# Output: ZeroDivisionError

# Código con órden correcto
print(cantidad != 0 and total / cantidad > 100)
# Output: False

# =====================================================================================

# Ejercicio 3: Tienes 137 libros y cajas de 12. Calcula cuántas cajas completas llenas 
# y cuántos libros quedan sueltos. Imprime ambos resultados con f-strings.

#---------------
# Pseudocódigo:
# 1. ¿Cuántos libros caben en las cajas? (Divisón entera)
# 2. ¿Cuántos libros sobran? (Residuo)
# --------------

cantidad_libros = 137
libros_por_caja = 12

print(f"Cantidad de libros totales:         {cantidad_libros}")
print(f"Cantidad de libros en cada caja:    {libros_por_caja}")
print(f"Cajas llenas:                       {cantidad_libros // libros_por_caja}")
print(f"Libros sobrantes:                   {cantidad_libros % libros_por_caja}")

# Ejercicio 4: Para un libro con existencias, precio, es_novedad (bool) y ventas_mes, 
# crea estas variables booleanas y imprime cada una:
# - requiere_reabasto: quedan menos de 5 ejemplares.
# - candidato_promocion: es novedad y cuesta más de 300.
# - sin_movimiento: no tuvo ventas en el mes y tiene más de 20 en existencia.
# - revisar: cumple cualquiera de las dos anteriores (candidato_promocion o sin_movimiento).

#---------------
# Pseudocódigo:
# 1. Obtener datos del título a valorar: existencias, precio, es_novedad, ventas_mes
# 2. Preguntar novedad y costo
# 3. Preguntar cuantas ventas tuvo en el mes y existencias
# 4. Confirmar si cumple con cualquiera de las condiciones novedad o movimiento
#---------------

existencias = int(input("¿Cuántos libros disponibles hay? "))
precio = float(input("Qué precio tiene el título? "))
es_novedad = input("¿Es novedad? (si/no)") == "si"
ventas_mes = int(input("¿Cuántas ventas tuvo en el mes? "))

requiere_reabasto = existencias < 5
candidato_promocion = es_novedad and precio > 300
sin_movimiento = ventas_mes == 0 and existencias > 20
revisar = candidato_promocion or sin_movimiento

print(f"¿Requiere reabasto?             {requiere_reabasto}")
print(f"¿Es candidato a promoción?      {candidato_promocion}")
print(f"Sin movimiento en este mes?    {sin_movimiento}")
print(f"¿Debe revisarse?                {revisar}")

# Ejercicio 5: Crea una variable isbn_valido que sea True solo si el ISBN tiene 
# 13 caracteres, y son todos dígitos, y empieza con 978 o con 979

#---------------
# Pseudocódigo:
# 1. Solicita ISBN
# 2. ¿Cuántos carácteres tiene el texto recibido? (len)
# 3. ¿Son todos los carácteres dígitos numéricos? (isdigit)
# 4. ¿Empieza con 978 o 979? ([X:X])
# 5. Valida si cumple con uno de los dos prefijos.
#---------------

isbn = "9786071612345"
# isbn = "978607161234"
# isbn = "97860716123X5"
# isbn = "1234567890123"

cantidad_caracteres = len(isbn)
son_digitos = isbn.isdigit()
prefijo = isbn[0:3]
inicio_valido = prefijo == "978" or prefijo == "979"

isbn_valido = cantidad_caracteres == 13 and son_digitos and (inicio_valido)

print(f"¿Es ISBN {isbn} válido?:  {isbn_valido}")