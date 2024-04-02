import serial
import serial.tools.list_ports as sr
import pandas as pd
import numpy as np
import threading
import time




valueList = []
BAUD = 9600

def get_ports():
    portList = [tuple(p) for p in list(sr.comports())]

    return portList


def aff_ports(portList):
    print("Avaiable PORT")
    print("----------------------------------")
    print(portList[0][1])
    print("----------------------------------")



def select_port(all_port):
    selected = "COM" + str(input("Select port : COM"))
    serialInst = serial.Serial(selected, BAUD, timeout=10)

    selected1 = [port for port in all_port if str(selected) in port][0]

    return selected1, serialInst



def verify_port(actual_port, interval = 0.1):
    while True:
        my_ports = [tuple(p) for p in list(sr.comports())]
        if actual_port not in my_ports:
            print("Arduino disconnected")
            break
        time.sleep(interval)



def main():
    all_ports = get_ports()
    aff_ports(get_ports())
    Port, serialInst = select_port(all_ports)
    port_controller = threading.Thread(target = verify_port, args = (Port, 0.1))
    port_controller.setDaemon(True)
    port_controller.start()


    while True:
        try:
            packet = serialInst.readline()
            valeur = packet.decode('utf')
            valueList.append(valeur)
            print(valeur)
        except serial.SerialException:
            serialInst.close()
            print("L'arduino a été déconnecté")
            break

    exc = pd.DataFrame(valueList).T
    exc.to_excel(excel_writer="output.xlsx")
if __name__ == '__main__':
    main()

