from datetime import datetime



class race():
    db = None
    RecordState = False

    def __init__(self, DB):
        self.db = DB

    def get_current_race_id(self):
        """Retourne l'ID de la course en cours, ou -1 si aucune course n'est en cours."""
        query = '''
        SELECT id FROM races
        WHERE end_time IS NULL
        ORDER BY start_time DESC
        LIMIT 1;
        '''
        result = self.db.fetch_results(query)

        return result[0][0] if result else -1



    def start_race(self):
            """Démarrer une nouvelle course en ajoutant une nouvelle entrée dans la table races."""
            start_time = datetime.now()
            query = '''
            INSERT INTO races (start_time)
            VALUES (?);
            '''
            params = (start_time,)
            self.db.execute_query(query, params)
            print("Nouvelle course démarrée")
            self.RecordState = True

    def end_race(self):
            """Mettre à jour la course en cours avec le temps de fin actuel."""
            end_time = datetime.now()
            race_id = self.get_current_race_id()
            if race_id == -1:
                print("Aucune course en cours à terminer.")
                return

            query = '''
            UPDATE races
            SET end_time = ?
            WHERE id = ?;
            '''
            params = (end_time, race_id)
            self.db.execute_query(query, params)
            print("Course terminée")
            self.RecordState = False