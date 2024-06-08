import Main
import api
from DataBase import DataBase
from input import Input
from Data.race import race
from Data.donne import donne
from basic import BasicGraph


db = DataBase("example.db")
course = None
data = None



def initDB():
    db.get_connection()  # Créer une connexion à la base de données


def get_all_donne():
    # Préparer la requête de sélection
    select_query = "SELECT * FROM donne;"

    # Exécuter la requête et récupérer les résultats
    results = db.fetch_results(select_query)

    return results

def get_all_donne_json():
    # Préparer la requête de sélection
    select_query = "SELECT * FROM donne;"

    # Exécuter la requête et récupérer les résultats
    results = db.fetch_results_as_json(select_query)

    return results




if __name__ == '__main__':

    initDB()
    #db.delete_all_tables()
    db.creatTable()
    course = race(db)
    Main.course = course
    Main.data =  donne(db, course)
    Main.basicGraph = BasicGraph(Main.data)





    FakeArduino = Input(course)
    FakeArduino.Activate()

    api.app.run(host='0.0.0.0', port=5000)


