import time
import Main
from datetime import datetime
import threading
import random

class Input:
    UpdateTime = 0.1  # Durée souhaitée pour chaque frame en secondes
    race = None

    def __init__(self, Race):
        self.i = 0
        self.race = Race

    def Activate(self):
        print("Activate Input")
        # Créer un thread détaché (daemon thread)
        thread = threading.Thread(target=self.Update, daemon=True)
        print("Objet thread créé")
        thread.start()
        print("Thread démarré")


    def Update(self):
        print("update")

        while True:
            print("boucle")
            start_time = time.time()  # Temps de début de la frame
            if self.race.RecordState:
                strain_gage_5 = random.uniform(0, 1)  # Variation aléatoire entre 0 et 1
                strain_gage_6 = random.uniform(0, 1)
                strain_gage_7 = random.uniform(0, 1)
                rpm_counter1 = random.randint(500, 3000)  # Variation aléatoire entre 500 et 3000
                speed_counter = random.uniform(0, 50)  # Variation aléatoire entre 0 et 50
                accel_1_y = random.uniform(-10, 10)
                accel_1_x = random.uniform(-10, 10)

                params = {
                    'strain_gage_1': 0, 'strain_gage_2': 0, 'strain_gage_3': 0, 'strain_gage_4': 0,
                    'strain_gage_5': strain_gage_5,
                    'strain_gage_6': strain_gage_6, 'strain_gage_7': strain_gage_7, 'strain_gage_8': 0, 'strain_gage_9': 0, 'strain_gage_10': 0,
                    'strain_gage_11': 0, 'strain_gage_12': 0, 'strain_gage_13': 0, 'strain_gage_14': 0,
                    'strain_gage_15': 0,
                    'strain_gage_16': 0, 'strain_gage_17': 0, 'strain_gage_18': 0, 'strain_gage_19': 0,
                    'strain_gage_20': 0,
                    'strain_gage_21': 0, 'strain_gage_22': 0, 'strain_gage_23': 0, 'strain_gage_24': 0,
                    'strain_gage_25': 0,
                    'strain_gage_26': 0, 'strain_gage_27': 0, 'strain_gage_28': 0, 'strain_gage_29': 0,
                    'strain_gage_30': 0,
                    'strain_gage_31': 0, 'strain_gage_32': 0, 'strain_gage_33': 0, 'strain_gage_34': 0,
                    'strain_gage_35': 0,
                    'strain_gage_36': 0, 'strain_gage_37': 0, 'strain_gage_38': 0, 'strain_gage_39': 0,
                    'strain_gage_40': 0,
                    'strain_gage_41': 0, 'strain_gage_42': 0, 'strain_gage_43': 0, 'strain_gage_44': 0,
                    'strain_gage_45': 0,
                    'strain_gage_46': 0, 'strain_gage_47': 0, 'strain_gage_48': 0, 'strain_gage_49': 0,
                    'strain_gage_50': 0,
                    'accelerometer': 0, 'rpm_counter1': rpm_counter1, 'rpm_counter2': 0, 'speed_counter': speed_counter,
                    'race_id': None,
                    'accel_1_x': accel_1_x, 'accel_1_y': accel_1_y, 'accel_1_z': 0, 'accel_1_rot_x': 0, 'accel_1_rot_y': 0,
                    'accel_1_rot_z': 0,
                    'accel_2_x': 0, 'accel_2_y': 0, 'accel_2_z': 0, 'accel_2_rot_x': 0, 'accel_2_rot_y': 0,
                    'accel_2_rot_z': 0,
                    'accel_3_x': 0, 'accel_3_y': 0, 'accel_3_z': 0, 'accel_3_rot_x': 0, 'accel_3_rot_y': 0,
                    'accel_3_rot_z': 0,
                    'accel_4_x': 0, 'accel_4_y': 0, 'accel_4_z': 0, 'accel_4_rot_x': 0, 'accel_4_rot_y': 0,
                    'accel_4_rot_z': 0,
                    'accel_5_x': 0, 'accel_5_y': 0, 'accel_5_z': 0, 'accel_5_rot_x': 0, 'accel_5_rot_y': 0,
                    'accel_5_rot_z': 0
                }

                print("Data added")
                Main.data.insert_sensor_data(params)



            print("update trig")
            end_time = time.time()  # Temps de fin de la frame
            frame_duration = end_time - start_time
            sleep_time = max(0, self.UpdateTime - frame_duration)

            if sleep_time > 0:
                time.sleep(sleep_time)

        # Vous pouvez ajouter d'autres opérations ici