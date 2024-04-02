import serial
import pandas as pd
import numpy as np

#ser = serial.Serial("COM3", 9600)
Value = np.zeros(10)

for i in range(10):
    Value[i] = 1

#while(True) :
   # Value.append(str(ser.readline()))

exc = pd.DataFrame(Value).T
exc.to_excel(excel_writer="output.xlsx")

