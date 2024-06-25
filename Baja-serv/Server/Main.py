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
    db.creatTable()
    course = race(db)
    Main.course = course
    Main.data = donne(db, course)
    Main.basicGraph = BasicGraph(Main.data)



    #FakeArduino = Input(course)
    #FakeArduino.Activate()

    #context = ('./SSL/cert.pem', './SSL/key.pem')
    #api.app.run(host='0.0.0.0', port=5000,ssl_context = context )

    import threading
    import ssl

    context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    context.load_cert_chain('./SSL/cert.pem', './SSL/key.pem')


    def run_https():
        api.app.run(host='0.0.0.0', port=5000, ssl_context=context) #http server pour unity car besoin SSL

    def run_http():
        api.app.run(host='0.0.0.0', port=80)


    https_thread = threading.Thread(target=run_https)
    http_thread = threading.Thread(target=run_http)

    https_thread.start()
    http_thread.start()

    https_thread.join()
    http_thread.join()


