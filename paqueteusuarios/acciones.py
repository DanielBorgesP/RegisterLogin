import paqueteusuarios.usuario as modelo
import paquetenotas.acciones

class Acciones:

    def registro(self):
        print("\nOk! Vamos a registrate en el sistema...")

        nombre = input("Cual es tu nombre?: ")
        apellidos = input("Cual es tu apellido?: ")
        email = input("Introduce tu email: ")
        password = input("Introduce tu contrasena: ")

        usuario = modelo.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        
        if registro[0] >= 1:
            print(f"Perfecto {registro[1].nombre} te has registrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente")
        
    def login(self):
        print("\nVale! Identificate en el sistema...")


        try: 
            email = input("Introduce tu email: ")
            password = input("Introduce tu contrasena: ")

            usuario = modelo.Usuario('','',email,password)
            login = usuario.identificar()

            if email == login[3]:
                print(f"Bienvenido {login[1]}, te has registrado en el sistema")
                self.proximasAcciones(login)
        except Exception as e:
            print(type(e))
            print(type(e).__name__)
            print(f"Login incorrecto!! Intentalo mas tarde")

    def proximasAcciones(self, usuario):
        print("""
        Acciones disponibles
        - Crear notas (crear)
        - Mostrar tus notas (mostrar)
        - Eliminar notas (eliminar)
        - Salir (salir)
        """)

        accion = input("Que quieres hacer?")
        hazEl = paquetenotas.acciones.Acciones()
        
        if accion == "crear":
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        elif accion == "mostrar":
            hazEl.mostrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "eliminar":
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)
        elif accion == "salir":
            exit()