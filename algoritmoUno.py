#Entradas del sistema
nombre_usuario=input("Digite su nombre 🤌: ")
correo_usuario=input("Digiter su correo electronico ✉️: ")
contraseña_usuario=input("Registre su contraseña 🔑: ")
ciudad_usuario=input("Ingrese su ciudad 🏙️: ")
edad_usuario=input("Ingrese su edad ⌛: ")

correo_bd="prueba@gmail.com"
contraseña_bd="admin123"

#Condicional en python
if(correo_usuario == correo_bd and contraseña_usuario == contraseña_bd):
    print("Bienvenido al sistema 🆗")
else:
    print("Datos ingresados no validos ⛔")