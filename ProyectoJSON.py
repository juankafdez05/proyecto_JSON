import json

def GanadoresBalonDeOro(doc):
    ano_gan = int(input("Introduzca el año :" ))
    gana = []
    
    for ganadores in doc["balon_de_oro"]["ganadores"]:
        if ganadores["año"] == ano_gan:
            gana.append(ganadores["jugador"]["nombre"])
    
    return gana
    

 

with open("JSONproyecto") as fichero:
    doc=json.load(fichero)

#Ejercicio 1

print("¿Que año quieres consultar?")

for gana in GanadoresBalonDeOro(doc):
    if gana != 0 :
        print("El ganador el fue: ", gana)