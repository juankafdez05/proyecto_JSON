
import json



def GanadoresBalonDeOro(doc):
    ano_gan = int(input("Introduzca el año :" ))
    gana = []
    
    for ganadores in doc["balon_de_oro"]["ganadores"]:
        if ganadores["año"] == ano_gan:
            gana.append(ganadores["jugador"]["nombre"])
    
    return gana
    
def MedioCentrosGanadores(doc):
    medio= []
    posiciones_mediocentros = {"Mediocentro", "Centrocampista" , "Mediapunta" , "Mediocampista"}
    nombres_vistos = set()

    for ganadores in doc["balon_de_oro"]["ganadores"]:
        if ganadores["jugador"]["posicion"] in posiciones_mediocentros and ganadores["jugador"]["nombre"] not in nombres_vistos:
            
            medio.append(ganadores["jugador"]["nombre"])
            nombres_vistos.add(ganadores["jugador"]["nombre"])

    return medio
    

with open("JSONproyecto") as fichero:
    doc=json.load(fichero)

#Ejercicio 1

print("¿Que año quieres consultar?")

for gana in GanadoresBalonDeOro(doc):
    if gana != 0 :
        print("El ganador el fue: ", gana)

#Ejercicio 2

for medio in MedioCentrosGanadores(doc):
    print("El Balon de Oro siendo mediocentro lo han ganado", len(MedioCentrosGanadores(doc)), "Estos son: ", medio )
    print("Nombres:", ", ".join(MedioCentrosGanadores(doc)))
    
