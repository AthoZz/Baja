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

        while True:
            print("boucle")
            start_time = time.time()  # Temps de début de la frame
            if self.race.RecordState:
                strain_gage_5 = random.uniform(0, 1)  # Variation aléatoire entre 0 et 1
                rpm_counter1 = random.randint(500, 3000)  # Variation aléatoire entre 500 et 3000
                speed_counter = random.uniform(0, 50)  # Variation aléatoire entre 0 et 50

                print("Data added")
                Main.data.insert_sensor_data(strain_gage_5=strain_gage_5, rpm_counter1=rpm_counter1,
                                             speed_counter=speed_counter)



            print("update trig")
            end_time = time.time()  # Temps de fin de la frame
            frame_duration = end_time - start_time
            sleep_time = max(0, self.UpdateTime - frame_duration)

            if sleep_time > 0:
                time.sleep(sleep_time)

        # Vous pouvez ajouter d'autres opérations ici