import random

class Escenario:
    def __init__(self, descripcion, historia, opciones):
        self.descripcion = descripcion
        self.historia = historia
        self.opciones = opciones

def cambiar_escenario(numero_escenario, escenarios):
    print(escenarios[numero_escenario].descripcion)
    print(escenarios[numero_escenario].historia)

if __name__ == "__main__":
    num_escenarios = 20
    escenarios = [None] + [None] * num_escenarios

    random.seed()

    escenarios[1] = Escenario("Bosque Oscuro", "Te encuentras en un bosque oscuro. Hay un camino a la izquierda y una cueva a la derecha.", [2, 3])
    escenarios[2] = Escenario("Playa Soleada", "Ahora estás en una playa soleada. Puedes ver un barco a lo lejos.", [1, 4])
    escenarios[3] = Escenario("Cueva Misteriosa", "Entraste en la cueva y descubriste un pasadizo secreto. Hay una salida a la montaña.", [5, 1])
    escenarios[4] = Escenario("Barco Abandonado", "Llegas al barco y encuentras un mapa que te lleva a una isla misteriosa.", [2, 6])
    escenarios[5] = Escenario("Montaña Escarpada", "Subes la montaña y descubres una antigua fortaleza en ruinas.", [7, 3])
    escenarios[6] = Escenario("Isla Misteriosa", "La isla está llena de criaturas extrañas. Puedes explorar el bosque o la playa.", [8, 4])
    escenarios[7] = Escenario("Fortaleza en Ruinas", "Dentro de la fortaleza, encuentras un artefacto mágico. Puedes estudiarlo o continuar.", [9, 5])
    escenarios[8] = Escenario("Bosque Encantado", "El bosque emite un resplandor mágico. Hay un sendero luminoso y un lago cristalino.", [10, 6])
    escenarios[9] = Escenario("Biblioteca Antigua", "Dentro de la fortaleza, encuentras una biblioteca con libros antiguos. Puedes leer uno o salir.", [11, 7])
    escenarios[10] = Escenario("Claro Brillante", "En el claro, encuentras a seres mágicos. Puedes hablar con ellos o seguir adelante.", [12, 8])
    escenarios[11] = Escenario("Laboratorio Alquímico", "Dentro de la biblioteca, encuentras un laboratorio alquímico. Puedes experimentar o irte.", [13, 9])
    escenarios[12] = Escenario("Reino de las Hadas", "Los seres mágicos te llevan al reino de las hadas. Puedes quedarte o regresar.", [14, 10])
    escenarios[13] = Escenario("Pasadizo Subterráneo", "El laboratorio tiene un pasadizo secreto. Puedes explorar o volver atrás.", [15, 11])
    escenarios[14] = Escenario("Palacio de las Hadas", "En el reino de las hadas, te invitan al palacio. Puedes aceptar o declinar.", [16, 12])
    escenarios[15] = Escenario("Cámara Antigua", "El pasadizo te lleva a una cámara antigua. Puedes investigar o regresar.", [17, 13])
    escenarios[16] = Escenario("Cima de la Montaña", "Desde el palacio, subes a la cima. Puedes contemplar la vista o descender.", [18, 14])
    escenarios[17] = Escenario("Sala de los Secretos", "En la cámara, encuentras información secreta. Puedes usarla o continuar.", [19, 15])
    escenarios[18] = Escenario("Valle Sereno", "Desde la cima, llegas a un valle sereno. Puedes descansar o seguir explorando.", [20, 16])
    escenarios[19] = Escenario("Templo Olvidado", "La información te lleva a un templo olvidado. Puedes entrar o ignorarlo.", [17, 18])
    escenarios[20] = Escenario("Final Épico", "Después de explorar, llegas a un enfrentamiento épico. ¡Prepárate para la batalla final!", [19])

    escenario_actual = 1

    print("¡Bienvenido a la historia gráfica!")

    while escenario_actual <= num_escenarios:
        print("Opciones:")
        for i, opcion in enumerate(escenarios[escenario_actual].opciones, start=1):
            print(f"{i}. {escenarios[opcion].descripcion}")
        print("0. Salir de la historia.")

        opcion = int(input("Elige una opción: "))  

        if opcion == 0:
            print("¡Gracias por jugar! Fin de la historia.")
            break

        if 1 <= opcion <= len(escenarios[escenario_actual].opciones):
            escenario_actual = escenarios[escenario_actual].opciones[opcion - 1]
            cambiar_escenario(escenario_actual, escenarios)
        else:
            print("Opción no válida. Inténtalo de nuevo.")

    print("¡Has explorado todos los escenarios! Fin de la historia.")
