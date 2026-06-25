#Crear un algoritmo que clasifique el estado de la prenda
#Si es regular le asigana un puntaje de 20, si es bueno de 50, si es optimo de 100 y roto de 1

estado_prenda=input("Digita el estado de la prende: ").upper()

valor_prenda=None
if estado_prenda == "REGULAR":
    valor_prenda=20
    print(valor_prenda)
elif estado_prenda == "BUENO":
    valor_prenda=50
    print(valor_prenda)
elif estado_prenda == "OPTIMO":
    valor_prenda=100
    print(valor_prenda)
elif estado_prenda == "ROTO":
    valor_prenda=1
    print(valor_prenda)
else:
    print("Valor ingresado no valido")