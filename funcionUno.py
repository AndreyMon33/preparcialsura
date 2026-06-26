#Funcion para evaluar correos y contraseñas

def ingresar_usuario(correo,contraseña,nobre,edad,ciudad):
    correo_bd="prueba@gmail.com"
    contraseña_bd="admin123"

    if(correo == correo_bd and contraseña == contraseña_bd):
        return("Bienvenido al sistema 🆗")
    else:
        return("Datos ingresados no validos ⛔")
