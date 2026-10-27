## Notas

**¿Por qué el correo de git config debe ser el mismo que el de GitHub?**
R: Para utilizarlo como identificador en las contribuciones de la cuenta que se enlace al repositorio.

**¿Qué diferencia hay entre guardar un archivo y hacer un commit?
R: El uso de guardar archivo sobrescribe el archivo a su versión más reciente y la anterior desaparece, mientras que commit realiza una fotografía del estatus actual del archivo, para reversiones a puntos específicos del repositorio.

**¿Para que existe el staging, si Git podría simplemente guardar todo lo que cambió?**
R: Para seccionar y controlar los cambios realizados por periodos y tareas específicas, con fin de no mezclar distintos procesos de trabajo en un solo commit y facilitar su identificación.

**Qué información guarda un commit además de los cambios en los archivos?**
R: Hora, fecha, autor, y mensaje del commit. Adicionalmente en detalle, guarda el tree, parent y commiter.

**¿Por qué no deberías subir los Excel reales de tu trabajo a un repo público, y por qué no basta con borrarlos después si se te escaparon?**
R: Porque contienen información sensible de la empresa, con confidencialidad. No basta con borrarlos después porque la información aún continuaría agregada en commits pasados.

**¿Qué hace -u y por qué solo se usa la primera vez?**
R: Permite establecer una conexión entre la rama local y la rama main del repositorio para evitar situar argumentos en cada ocasión que se realice una carga a través de *push*.

**Qué pasaría si haces *push* sin haber hecho *pull* de un cambio remoto?
R: El push es rechazado debido a que no puede empatar los cambios nuevos que incluye la rama local al remoto. Requiere pull para importar los cambios que contiene el repositorio remoto, y hacer una fusión con los cambios del local.
