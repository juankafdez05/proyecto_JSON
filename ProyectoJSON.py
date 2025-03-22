import json
import FuncionesJSON

def main():

    while True:

        with open("JSONproyecto") as fichero:
            
            doc=json.load(fichero)

        print("\n=== Balón De Oro ===\n")
        print("1. Ganadores del Balón de Oro\n")
        print("2. Mediocentros ganadores\n")
        print("3. Filtrar por posición\n")
        print("4. Filtrar por jugador\n")
        print("5. Top 5 jugadores con más goles generados\n")
        print("0. Salir\n")

        choice = input("Introduce tu opción (0-5): ")

        if choice == '1':

            print("¿Que año quieres consultar?")
            
            for gana in FuncionesJSON.GanadoresBalonDeOro(doc):
              if gana != 0 :
                print("El ganador el fue: ", gana)

        elif choice == '2':

            for medio in FuncionesJSON.MedioCentrosGanadores(doc):
                print("El Balon de Oro siendo mediocentro lo han ganado", len(FuncionesJSON.MedioCentrosGanadores(doc)), "Estos son: ",)
                print("Nombres:\n", " \n".join(FuncionesJSON.MedioCentrosGanadores(doc)))


        elif choice == '3':
        
            if FuncionesJSON.filtrarposición(doc):
                print("\nLos ganadores del balon de oro en esa posicion son:\n")
                print ("\n".join(FuncionesJSON.filtrarposición(doc)))
            else:
                print("No se han encontrado ganadores en esa posición")

        elif choice == '4':
           
           if FuncionesJSON.filtrarjugador(doc):
            print("\nEsta es la informacion disponible del jugador buscado:\n")
            print("\n".join(FuncionesJSON.filtrarjugador(doc)))
            print(f"\nTotal de veces ganado: {len(FuncionesJSON.filtrarjugador(doc))}")
           else:
              print("No se ha encontrado información para ese jugador")

        elif choice == '5':
            if FuncionesJSON.top5(doc):
                print("Los 5 ganadores con más goles generados en su carrera son:\n")
                print("\n".join(FuncionesJSON.top5(doc)))


        elif choice == '0':

            print("Saliendo del programa.")

            break

        else:

            print("Opción no válida. Por favor, intenta de nuevo.")
            continue

if __name__ == "__main__":
    
    main()
