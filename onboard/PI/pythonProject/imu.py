import json
import serial
import time


serial = serial.Serial('COM3', 115200, timeout = 1)

print('allO')
#time.sleep(5)

while True:
    time.sleep(1)
    try:
        if serial.in_waiting >0:

            raw_data = serial.readline().decode('utf-8').strip()
            data = json.loads(raw_data)
            print(raw_data)
            print(f"X : {data['x']}")
            print(f"Y : {data['y']}")
            print(f"Z : {data['z']}")

    except json.JSONDecodeError:
        print("Error decoding JSON data")
        break
print(2)
serial.close()
