"""
Proyecto Python y Mysql:
- Abrir asistente.
- Login o registro.
- Si elegimos registro, creara un usuario en la base de datos.
- Crear nota, mostrar notas, borrarlas.
"""

from paqueteusuarios import acciones

print("""
Acciones disponibles:

    - registro
    - login
""")

hazEl = acciones.Acciones()
accion = input("Que quieres hacer?: ")

if accion == "registro":
    hazEl.registro()
elif accion == "login":
    hazEl.login()
