## Notas de sesiones

### Github

**¿Por qué el correo de git config debe ser el mismo que el de GitHub?**

R: Para utilizarlo como identificador en las contribuciones de la cuenta que se enlace al repositorio.

**¿Qué diferencia hay entre guardar un archivo y hacer un commit?**

R: El uso de guardar archivo sobrescribe el archivo a su versión más reciente y la anterior desaparece, mientras que commit realiza una fotografía del estatus actual del archivo, para reversiones a puntos específicos del repositorio.

**¿Para que existe el staging, si Git podría simplemente guardar todo lo que cambió?**

R: Para seccionar y controlar los cambios realizados por periodos y tareas específicas, con fin de no mezclar distintos procesos de trabajo en un solo commit y facilitar su identificación.

**Qué información guarda un commit además de los cambios en los archivos?**

R: Hora, fecha, autor, y mensaje del commit. Adicionalmente en detalle, guarda el tree, parent y commiter.

**¿Por qué no deberías subir los Excel reales de tu trabajo a un repo público, y por qué no basta con borrarlos después si se te escaparon?**

R: Porque contienen información sensible de la empresa, con confidencialidad. No basta con borrarlos después porque la información aún continuaría agregada en commits pasados.

**¿Qué hace -u y por qué solo se usa la primera vez?**

R: Permite establecer una conexión entre la rama local y la rama main del repositorio para evitar situar argumentos en cada ocasión que se realice una carga a través de *push*.

**Qué pasaría si haces *push* sin haber hecho *pull* de un cambio remoto?**

R: El push es rechazado debido a que no puede empatar los cambios nuevos que incluye la rama local al remoto. Requiere pull para importar los cambios que contiene el repositorio remoto, y hacer una fusión con los cambios del local.

**Por qué trabajar en una rama en lugar de directamente en *main*?**

R: Para no afectar el código que ya funciona en main, o arriesgarlo. De esta forma se trabaja de forma ajena o indirectamente relacionada, para posibles pruebas de añadidos de herramientas, u optimizaciones.

**Qué te está diciendo Git cuando marca un conflicto?**

R: No necesariamente indica que existe un problema genuino, sino un choque entre versiones que requiere resolverse. Git no lo resuelve de forma autónoma porque requiere de toma de decisiones manual para la resolución.

### Python

1. ¿Qué diferencia hay entre la consola interactiva y un script? ¿Por qué 2 + 3 muestra 5 en la consola pero no muestra nada en un script?

R: La consola interactiva resuelve los argumentos de lógica y los imprime, pero un script requiere de solicitud de impresión para dar el resultado en lugar de resolverlo y descartarlo. La consolta interactiva lleva por nombre REPL (Read, Eval, Print, Loop).

2. Un ISBN como 9786071612345 está formado solo por dígitos. ¿Por qué conviene guardarlo como str y no como int?

R: Porque funge como un identificador, y el identificador no necesita ser modificado de ninguna forma mediante operadores matemáticos.

3. En el Paso 3 Sesión 3, ¿por qué una versión da error y la otra no, si las dos condiciones son exactamente las mismas?

R: Porque primero verifica que la condición se cumpla, y como ZeroDivision Error no permite llegar a la verificación booleanea, al invertir los valores, y cumplirse la condición como False, detiene la división y evita el lanzamiento de error.