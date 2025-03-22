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

def filtrarposición(doc):
    posicion= []
    posicion_buscada = input("Introduzca sobre que posición desea conocer los ganadores: ").strip()
    grupos = {    
        "Mediocentro": {"Mediocentro", "Centrocampista" , "Mediapunta" , "Mediocampista"},
        "Defensa": {"Defensa"},
        "Delantero": {"Delantero","Exremo"},
        "Portero": {"Portero"}
    }

    posiciones_a_buscar = grupos.get(posicion_buscada, {posicion_buscada})

    nombres_vistos = set()

    for ganadores in doc["balon_de_oro"]["ganadores"]:

        nombre= ganadores["jugador"]["nombre"]
        pos_jugador= ganadores["jugador"]["posicion"]

        if pos_jugador in posiciones_a_buscar and nombre not in nombres_vistos:
           
        
            posicion.append(nombre)
            nombres_vistos.add(nombre)
    return posicion

    
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


def top5(doc):
    jugadores = {}  

    for ganador in doc["balon_de_oro"]["ganadores"]:
        nombre = ganador["jugador"]["nombre"]
        año_actual = ganador["año"]
        goles = ganador["jugador"]["carrera"]["estadisticas"]["goles"]
        asistencias = ganador["jugador"]["carrera"]["estadisticas"]["asistencias"]
        
        if nombre not in jugadores or año_actual > jugadores[nombre]["año"]:
            jugadores[nombre] = {
                "año": año_actual,
                "goles": goles,
                "asistencias": asistencias,
                "total": goles + asistencias
            }

    jugadores_ordenados = sorted(
        jugadores.items(),
        key=lambda x: x[1]["total"],
        reverse=True
    )[:5]

    generados = []
    for nombre, stats in jugadores_ordenados:
        generados.append(
            f"Jugador: {nombre}\n"
            f"Goles: {stats['goles']}\n"
            f"Asistencias: {stats['asistencias']}\n"
            f"Total generados: {stats['total']}\n"
            "---------------------"
        )

    return generados



