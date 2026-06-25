#Necesito crear un programa en python que me permita registrar 5 prendas de vestir
#producto_Uno = str(input("Digita el nombre del producto 1: "))
#producto_Dos = str(input("Digita el nombre del producto 2: "))
#producto_Tres = str(input("Digita el nombre del producto 3: "))
#producto_Cuatro = str(input("Digita el nombre del producto 4: "))
#producto_Cinco = str(input("Digita el nombre del producto 5: "))

#print(f"Los productos ingresados fueron: {producto_Uno}, {producto_Dos}, {producto_Tres}, {producto_Cuatro} y {producto_Cinco}")

#marca_uno = str(input("Ingrese el nombre de la priemra marca: "))
#marca_dos = str(input("Ingrese el nombre de la segunda marca: "))
#marca_tres = str(input("Ingrese el nombre de la tercera marca: "))

#print(f"Las marcas registradas son: {marca_uno}, {marca_dos} y {marca_tres}")

#Necesito crear 1 000 000 prendas
#id
#tipo
#marca
#precio
#estado

import random

prendas = []
for i in range (100):
    prenda={
        "ID":random.randint(1,100),
        "Tipo":random.choice(["camiseta","Jean","Pantalon","correa","Zapato"]),
        "Marca":random.choice(["Arturo calle","albertoV05","Gorditos sexy","lolas","ardidas"]),
        "Precio":random.randint(20000,100000),
        "Estado":random.choice(["Roto","Regular","Optimo","Bueno"])
    }
    prendas.append(prenda)
print(prendas)