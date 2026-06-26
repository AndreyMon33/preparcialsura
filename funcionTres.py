#Funcion que decide sobre el valor de la prenda

def clasificar_prenda(estado):
    valor_prenda=None
    if estado == "REGULAR":
        valor_prenda=20
        return(valor_prenda)
    elif estado == "BUENO":
        valor_prenda=50
        return(valor_prenda)
    elif estado == "OPTIMO":
        valor_prenda=100
        return(valor_prenda)
    elif estado == "ROTO":
        valor_prenda=1
        return(valor_prenda)
    else:
        return("Valor ingresado no valido")