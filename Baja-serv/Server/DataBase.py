import sqlite3
from sqlite3 import Error
from flask import g
import json
from datetime import datetime, timedelta


class DataBase:
    def __init__(self, db_file):
        self.db_file = db_file

    def get_connection(self):
        """Créer une nouvelle connexion à la base de données SQLite."""
        conn = sqlite3.connect(self.db_file, check_same_thread=False)
        return conn

    def execute_query(self, query, params=None):
        """Exécute une requête SQL."""
        conn = self.get_connection()
        try:
            c = conn.cursor()
            if params:
                c.execute(query, params)
            else:
                c.execute(query)
            conn.commit()
            print("Requête exécutée avec succès")
        except Error as e:
            print(f"Erreur lors de l'exécution de la requête: {e}")
        finally:
            conn.close()

    def fetch_results(self, query, params=None):
        """Exécute une requête SQL et retourne les résultats."""
        conn = self.get_connection()
        try:
            c = conn.cursor()
            if params:
                c.execute(query, params)
            else:
                c.execute(query)
            return c.fetchall()
        except Error as e:
            print(f"Erreur lors de la récupération des résultats: {e}")
            return None
        finally:
            conn.close()

    def fetch_results_as_json(self, query, params=None):
        """Exécute une requête SQL et retourne les résultats sous forme de JSON."""
        conn = self.get_connection()
        try:
            c = conn.cursor()
            if params:
                c.execute(query, params)
            else:
                c.execute(query)
            rows = c.fetchall()
            # Récupérer les noms des colonnes
            column_names = [description[0] for description in c.description]
            # Créer une liste de dictionnaires
            results = []
            for row in rows:
                results.append(dict(zip(column_names, row)))
            return json.dumps(results)
        except Error as e:
            print(f"Erreur lors de la récupération des résultats: {e}")
            return None
        finally:
            conn.close()

    def delete_all_tables(self):
        """Supprime toutes les tables de la base de données, à l'exception des tables spéciales."""
        conn = self.get_connection()
        try:
            c = conn.cursor()
            # Désactiver temporairement les contraintes de clés étrangères
            c.execute("PRAGMA foreign_keys = OFF;")
            c.execute("SELECT name FROM sqlite_master WHERE type='table';")
            tables = c.fetchall()
            print(f"Tables trouvées: {tables}")  # Afficher les tables trouvées
            for table_name in tables:
                if table_name[0] != 'sqlite_sequence':  # Ignorer la table spéciale sqlite_sequence
                    print(f"Suppression de la table: {table_name[0]}")  # Afficher la table en cours de suppression
                    c.execute(f"DROP TABLE IF EXISTS {table_name[0]};")
            conn.commit()
            print("Toutes les tables ont été supprimées avec succès")
        except Error as e:
            print(f"Erreur lors de la suppression des tables: {e}")
        finally:
            # Réactiver les contraintes de clés étrangères
            c.execute("PRAGMA foreign_keys = ON;")
            conn.close()

    def insert_data(self, table, data):
        """Insère des données dans la table spécifiée."""
        conn = self.get_connection()
        try:
            c = conn.cursor()
            placeholders = ', '.join(['?'] * len(data))
            columns = ', '.join(data.keys())
            sql = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            c.execute(sql, tuple(data.values()))
            conn.commit()
            print("Données insérées avec succès")
        except Error as e:
            print(f"Erreur lors de l'insertion des données: {e}")
        finally:
            conn.close()

    def creatTable(self):
        create_table_query_donne = """
          CREATE TABLE IF NOT EXISTS sensors_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            timestamp TEXT DEFAULT (strftime('%Y-%m-%d %H:%M:%f', 'now')),
            strain_gage_1 REAL,
            strain_gage_2 REAL,
            strain_gage_3 REAL,
            strain_gage_4 REAL,
            strain_gage_5 REAL,
            strain_gage_6 REAL,
            strain_gage_7 REAL,
            strain_gage_8 REAL,
            strain_gage_9 REAL,
            strain_gage_10 REAL,
            strain_gage_11 REAL,
            strain_gage_12 REAL,
            strain_gage_13 REAL,
            strain_gage_14 REAL,
            strain_gage_15 REAL,
            strain_gage_16 REAL,
            strain_gage_17 REAL,
            strain_gage_18 REAL,
            strain_gage_19 REAL,
            strain_gage_20 REAL,
            strain_gage_21 REAL,
            strain_gage_22 REAL,
            strain_gage_23 REAL,
            strain_gage_24 REAL,
            strain_gage_25 REAL,
            strain_gage_26 REAL,
            strain_gage_27 REAL,
            strain_gage_28 REAL,
            strain_gage_29 REAL,
            strain_gage_30 REAL,
            strain_gage_31 REAL,
            strain_gage_32 REAL,
            strain_gage_33 REAL,
            strain_gage_34 REAL,
            strain_gage_35 REAL,
            strain_gage_36 REAL,
            strain_gage_37 REAL,
            strain_gage_38 REAL,
            strain_gage_39 REAL,
            strain_gage_40 REAL,
            strain_gage_41 REAL,
            strain_gage_42 REAL,
            strain_gage_43 REAL,
            strain_gage_44 REAL,
            strain_gage_45 REAL,
            strain_gage_46 REAL,
            strain_gage_47 REAL,
            strain_gage_48 REAL,
            strain_gage_49 REAL,
            strain_gage_50 REAL,
            accelerometer REAL,
            rpm_counter1 INTEGER,
            rpm_counter2 INTEGER,
            speed_counter REAL,
            race_id INTEGER DEFAULT -1,
            accel_1_x REAL, accel_1_y REAL, accel_1_z REAL, accel_1_rot_x REAL, accel_1_rot_y REAL, accel_1_rot_z REAL,
            accel_2_x REAL, accel_2_y REAL, accel_2_z REAL, accel_2_rot_x REAL, accel_2_rot_y REAL, accel_2_rot_z REAL,
            accel_3_x REAL, accel_3_y REAL, accel_3_z REAL, accel_3_rot_x REAL, accel_3_rot_y REAL, accel_3_rot_z REAL,
            accel_4_x REAL, accel_4_y REAL, accel_4_z REAL, accel_4_rot_x REAL, accel_4_rot_y REAL, accel_4_rot_z REAL,
            accel_5_x REAL, accel_5_y REAL, accel_5_z REAL, accel_5_rot_x REAL, accel_5_rot_y REAL, accel_5_rot_z REAL
        );
        """
        self.execute_query(create_table_query_donne)

    def get_data_last_5_minutes(self):
        """Récupère les données des 5 dernières minutes."""
        conn = self.get_connection()
        try:
            c = conn.cursor()
            five_minutes_ago = datetime.now() - timedelta(minutes=5)
            query = """
                SELECT timestamp, strain_gage_1, accelerometer, rpm_counter1, rpm_counter2, speed_counter, race_id
                FROM sensors_data
                WHERE timestamp >= ?
                ORDER BY timestamp DESC
            """
            c.execute(query, (five_minutes_ago,))
            rows = c.fetchall()
            # Récupérer les noms des colonnes
            column_names = [description[0] for description in c.description]
            # Créer une liste de dictionnaires
            results = []
            for row in rows:
                results.append(dict(zip(column_names, row)))
            return results
        except Error as e:
            print(f"Erreur lors de la récupération des résultats: {e}")
            return None
        finally:
            conn.close()

    def getLasvalueStaing(self, strain_gage_id):
        """Récupère la dernière valeur pour la colonne strain_gage spécifique."""
        if not (1 <= strain_gage_id <= 50):
            raise ValueError("strain_gage_id doit être compris entre 1 et 50")

        column_name = f'strain_gage_{strain_gage_id}'
        conn = self.get_connection()
        try:
            c = conn.cursor()
            query = f"""
                       SELECT {column_name}
                       FROM sensors_data
                       ORDER BY timestamp DESC
                       LIMIT 1
                   """
            c.execute(query)
            row = c.fetchone()
            if row:
                return {"strain_gage": row[0]}
            else:
                return {"strain_gage": None}
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération de la valeur: {e}")
            return {"strain_gage": None}
        finally:
            conn.close()
    def getLasvalueAccelerationsG(self, imu_id): #non tester
        """Récupère les données d'accélération pour un ID donné et les convertit en g."""
        conn = self.get_connection()
        if conn is None:
            return None
        try:
            c = conn.cursor()

            # Détermine les noms de colonnes dynamiquement en fonction de l'ID
            accel_x_col = f"accel_{imu_id}_x"
            accel_y_col = f"accel_{imu_id}_y"
            accel_z_col = f"accel_{imu_id}_z"

            query = f"""
                        SELECT {accel_x_col}, {accel_y_col}, {accel_z_col}
                        FROM sensors_data
                        WHERE id = ?
                    """
            c.execute(query, (imu_id,))
            row = c.fetchone()
            if row is None:
                print(f"Aucune donnée trouvée pour l'ID: {imu_id}")
                return None

            # Extraction des valeurs d'accélération
            accel_x, accel_y, accel_z = row[0], row[1], row[2]

            # Conversion en g
            accel_x_g = self.convert_to_g(accel_x)
            accel_y_g = self.convert_to_g(accel_y)
            accel_z_g = self.convert_to_g(accel_z)

            return {
                "accel_x_g": accel_x_g,
                "accel_y_g": accel_y_g,
                "accel_z_g": accel_z_g
            }
        except sqlite3.Error as e:
            print(f"Erreur lors de la récupération des données: {e}")
            return None
        finally:
            conn.close()

    def convert_to_g(self, value):
        """Convertit une valeur d'accélération de m/s² en g."""
        return value / 9.81


