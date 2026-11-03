# Glosario de comandos

- 'git init': Crea la carpeta oculta .git donde vive el historial de commits.
- 'git status': Imprime el estatus actual del repositorio y sus archivos modificados.
- 'git add': Inicia la etapa staging, actualiza en el repositorio los cambios realizados en los archivos desde el último staging.
- 'git diff': Realiza un comparativo con la última modificación que tuvo el archivo antes de realizar 'add'
- 'git diff --staged': Realiza un comparativo con el estatus del último commit realizado.
- 'git restore --staged': Restaura el archivo añadido a 'add' con el estatus del último commit realizado.
- 'git show': Muestra los últimos cambios realizados del último commit
- 'git log': Muestra y descripción de los últimos registros de commit.
- 'git push': Empuja la información local hacia la rama elegida en el repositorio para guardado en la nube.
- 'git fetch': Importa los commits externos realizados al repositorio para verificación antes de importar los cambios con pull.
- 'git branch': Lista en pantalla las ramas disponibles en el repositorio y sobre cual estás posicionado.
- 'git switch': Crea o cambia a la rama seleccionada.
- 'git merge': Realiza la unión de los cambios de las branch por medio de la main que lo solicita.
- 'git pull': Extrae los cambios cargados al repositorio con el commit más actual.
- 'git clone': Realiza la copia de un repositorio en el directorio puesto.

## Sub-comandos

- 'git restore *archivo*': Restaura un archivo que aún no es procesado por commit
- 'git restore --stage *archivo*: Restaura un archivo que ya se proceso en stage con *add*
- 'git commit --amend': Restaura el estatus del último commit antes del cargarse al repositorio con push
- 'git revert *hash*: Revierte el último commit ya cargado al repositorio.