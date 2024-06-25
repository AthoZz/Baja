import requests
import json
import time

url = "http://100.107.141.200/add-data"

# Exemple de données à envoyer
data = {
    'strain_gage_1': 0,
    'strain_gage_2': 0,
    'strain_gage_3': 0,
    'strain_gage_4': 0,
    'strain_gage_5': 0,
    'strain_gage_6': 0,
    'strain_gage_7': 0,
    'strain_gage_8': 0,
    'strain_gage_9': 0,
    'strain_gage_10': 0,
    'strain_gage_11': 0,
    'strain_gage_12': 0,
    'strain_gage_13': 0,
    'strain_gage_14': 0,
    'strain_gage_15': 0,
    'strain_gage_16': 0,
    'strain_gage_17': 0,
    'strain_gage_18': 0,
    'strain_gage_19': 0,
    'strain_gage_20': 0,
    'strain_gage_21': 0,
    'strain_gage_22': 0,
    'strain_gage_23': 0,
    'strain_gage_24': 0,
    'strain_gage_25': 0,
    'strain_gage_26': 0,
    'strain_gage_27': 0,
    'strain_gage_28': 0,
    'strain_gage_29': 0,
    'strain_gage_30': 0,
    'strain_gage_31': 0,
    'strain_gage_32': 0,
    'strain_gage_33': 0,
    'strain_gage_34': 0,
    'strain_gage_35': 0,
    'strain_gage_36': 0,
    'strain_gage_37': 0,
    'strain_gage_38': 0,
    'strain_gage_39': 0,
    'strain_gage_40': 0,
    'strain_gage_41': 0,
    'strain_gage_42': 0,
    'strain_gage_43': 0,
    'strain_gage_44': 0,
    'strain_gage_45': 0,
    'strain_gage_46': 0,
    'strain_gage_47': 0,
    'strain_gage_48': 0,
    'strain_gage_49': 0,
    'strain_gage_50': 0,
    'accelerometer': 0,
    'rpm_counter1': 10,
    'rpm_counter2': 0,
    'speed_counter': 0,
    'race_id': None,
    'accel_1_x': 0,
    'accel_1_y': 0,
    'accel_1_z': 0,
    'accel_1_rot_x': 0,
    'accel_1_rot_y': 0,
    'accel_1_rot_z': 0,
    'accel_2_x': 0,
    'accel_2_y': 0,
    'accel_2_z': 0,
    'accel_2_rot_x': 0,
    'accel_2_rot_y': 0,
    'accel_2_rot_z': 0,
    'accel_3_x': 0,
    'accel_3_y': 0,
    'accel_3_z': 0,
    'accel_3_rot_x': 0,
    'accel_3_rot_y': 0,
    'accel_3_rot_z': 0,
    'accel_4_x': 0,
    'accel_4_y': 0,
    'accel_4_z': 0,
    'accel_4_rot_x': 0,
    'accel_4_rot_y': 0,
    'accel_4_rot_z': 0,
    'accel_5_x': 0,
    'accel_5_y': 0,
    'accel_5_z': 0,
    'accel_5_rot_x': 0,
    'accel_5_rot_y': 0,
    'accel_5_rot_z': 0
}

headers = {
    'Content-Type': 'application/json'
}

while True:
    try:
        response = requests.put(url, headers=headers, data=json.dumps(data))
        if response.status_code != 201:
            print(f"Failed to send data: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    time.sleep(0.01)  # 10 millisecondes
