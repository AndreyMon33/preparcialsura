#llamar funciones

import random

from funcionUno import ingresar_usuario
from funcionDos import crear_listado
from funcionTres import clasificar_prenda

ingresar_usuario("pepe@gmail.com","Estaesunacontraseña","externocleidomastoideo",999,"fondo de bikini")

prenda={
        "ID":random.randint(1,100),
        "Tipo":random.choice(["camiseta","Jean","Pantalon","correa","Zapato"]),
        "Marca":random.choice(["Arturo calle","albertoV05","Gorditos sexy","lolas","ardidas"]),
        "Precio":random.randint(20000,100000),
        "Estado":random.choice(["Roto","Regular","Optimo","Bueno"])
    }
crear_listado(10,prenda)

clasificar_prenda("REGULAR")