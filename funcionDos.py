#funcion que itera sobre una lista de usuarios

def crear_listado(numero_interaciones,prenda):
    prendas=[]

    for _ in range (numero_interaciones):
        prendas.append(prenda)
    return(prendas)