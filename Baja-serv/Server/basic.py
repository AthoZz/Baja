import matplotlib.pyplot as plt
import Main
from datetime import datetime
import io
class BasicGraph():

    def __init__(self, Data):
        self.data = Data

    def getGraphRPM1_5min(self):
        return self.genericGraph_5min('rpm_counter1')

    def getGraphRPM2_5min(self):
        return self.genericGraph_5min('rpm_counter2')

    def getGraphstrain_gage_5min(self):
        return self.genericGraph_5min('strain_gage_1')


    def genericGraph_5min(self, key):
        rawData = Main.db.get_data_last_5_minutes()
        return self.genericGraph(key, rawData)


    def genericGraph(self, key, Data):
        values = [entry[key] for entry in Data]
        timestamps = [datetime.fromisoformat(entry['timestamp']) for entry in Data]

        # Générer le graphique
        plt.figure()
        plt.plot(timestamps, values, marker='o')
        plt.xlabel('Time')
        plt.ylabel('Value')
        plt.title('Data Over Time')
        plt.gcf().autofmt_xdate()  # Pour formater les dates sur l'axe X

        # Enregistrer le graphique dans un objet BytesIO
        img = io.BytesIO()
        plt.savefig(img, format='png')
        img.seek(0)
        plt.close()

        return img

    def convert_to_g(self, value):
        """Convertit une valeur d'accélération de m/s² en g."""
        return value / 9.81
