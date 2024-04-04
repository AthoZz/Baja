import serial
import serial.tools.list_ports as sr
import pandas as pd
import time
import os


valueList = []
BAUD = 9600

# Cette fonction retoune tout les ports connectés à l'ordinateur sous forme de tableau
# de liste
def get_ports():
    portList = [tuple(p) for p in list(sr.comports())]
    return portList

# Cette fonction afficher les ports disponibles
def aff_ports(portList):
 
    print("Avaiable PORT")
    print("----------------------------------")
    if len(portList) == 0:
        print("None")
    if len(portList) > 0:
        print(portList[0][1]) # afin d'avoir seulement les informations comme COMx et non le reste qui ne nous importe pas
    print("----------------------------------")


# Cette fonction demande à l'utilisateur quel port il veut utiliser et retourne
# l'instantiation de la connection série qui sera utilse pour les prochaines étapes.

def select_port(all_port):
    # on demande à l'utilisateur à rentrer le numéro qui correspond au COM
    # sur lequel il veut se connecter, selected correspond alors à "COMx"
    # on vérifie également s'il y a des ports disponibles et se rafraichi si non

    while len(all_port) == 0:
        time.sleep(1)
        os.system('cls')
        aff_ports(all_port)
        all_port = get_ports()

    os.system('cls')
    aff_ports(get_ports())
    # selected correspond a COMx
    selected = "COM" + str(input("Select port : COM"))

    # on créer une connection série avec ce port
    serialInst = serial.Serial(selected, BAUD, timeout=10)

    return serialInst


def main():
    # all_ports correspond à une liste de tout les ports sur l'ordinateur
    all_ports = get_ports()
    # affiche les ports disponibles
    #aff_ports(get_ports())

    # retourne l'instantiation de la connection série
    serialInst = select_port(all_ports)

    # cette boucle répète ce qui est dans try tant que serial.SerialException n'est pas détecté,
    # dans le cas échéant, on ferme la connection et on sort de la boucle while

    while True:
        try:
            # le packet correspond à une ligne dans le serial
            # on décode en utf pour avoir la bonne valeur
            packet = serialInst.readline()
            valeur = packet.decode('utf')

            # on ajoute cette valeur à un tableau appelé : valueList qui sera ensuite converti en excel
            valueList.append(valeur)
            print(valeur)

        except serial.SerialException:
            serialInst.close()
            print("L'arduino a été déconnecté")
            break

    # lorsque l'on sort du while en raison de la déconnection de l'Arduino,
    # on prend les données de la liste valueList et on les converti en document
    # excel avec le nom "output.xlsx" qui apparaitra dans le meme fichier
    # que le code python une fois le scrip terminé

    exc = pd.DataFrame(valueList).T
    exc.to_excel(excel_writer="output.xlsx")


if __name__ == '__main__':
    main()

