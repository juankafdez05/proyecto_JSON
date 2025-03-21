
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
    
def filtrarjugador(doc):
    jugador_buscado = input("Introduzca el jugador que desas buscar información: ")
    jug= []
    años_vistos= set()

    for ganadores in doc["balon_de_oro"]["ganadores"]:
        if ganadores["jugador"]["nombre"] ==jugador_buscado:
            año= ganadores["año"]    

            if año not in años_vistos:

                equipos= ", ".join(ganadores["jugador"]["carrera"]["equipos"])

                goles = ganadores["jugador"]["carrera"]["estadisticas"]["goles"]

                asistencias = ganadores["jugador"]["carrera"]["estadisticas"]["asistencias"]
               
                info = (
                   
                   f"Año: {año}\n"
                   f"Equipos: {equipos}\n"
                   f"Goles: {goles}\n"
                   f"Asistencias: {asistencias}\n"
               )
                
            jug.append(info)
            años_vistos.add(año)

    return jug

with open("JSONproyecto") as fichero:
    doc=json.load(fichero)

#Ejercicio 1

#print("¿Que año quieres consultar?")

#for gana in GanadoresBalonDeOro(doc):
  #  if gana != 0 :
   #     print("El ganador el fue: ", gana)

#Ejercicio 2

#for medio in MedioCentrosGanadores(doc):
#print("El Balon de Oro siendo mediocentro lo han ganado", len(MedioCentrosGanadores(doc)), "Estos son: ",)
#print("Nombres:\n", " \n".join(MedioCentrosGanadores(doc)))

#Ejercico 3

resultados3 = filtrarjugador(doc)

if resultados3:
    print("\nEsta es la informacion disponible del jugador buscado:\n")
    print("\n".join(resultados3))
    print(f"\nTotal de veces ganado: {len(resultados3)}")
else:
    print("No se ha encontrado información para ese jugador")
