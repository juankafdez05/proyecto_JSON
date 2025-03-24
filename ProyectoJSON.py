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
                print("El ganador fue: ", gana)

        elif choice == '2':

            resultado2 = FuncionesJSON.MedioCentrosGanadores(doc)

            if resultado2:
                print("El Balon de Oro siendo mediocentro lo han ganado", len(resultado2), "Estos son: ",)
                print("Nombres:\n", " \n".join(resultado2))
            else:
                print("No se han encontrado ganadores en esa posición.")

        elif choice == '3':

            resultado3= FuncionesJSON.filtrarposición(doc)
        
            if resultado3:
                print("\nLos ganadores del balon de oro en esa posicion son:\n")
                print ("\n".join(resultado3))
            else:
                print("No se han encontrado ganadores en esa posición")

        elif choice == '4':
           
           resultado4 = FuncionesJSON.filtrarjugador(doc)
           if resultado4:
                print("Esta es la informacion disponible del jugador buscado:\n")
                print("\n".join(resultado4))
                print(f"\nTotal de veces ganado: {len(resultado4)}")
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
