from datetime import datetime

class donne():
    db = None
    race = None

    def __init__(self, DB, Race):
        self.db = DB
        self.race = Race

    def insert_sensor_data(self, params):
        #def insert_sensor_data(self, params):
        """Insère des données dans la table sensors_data avec l'ID de la course en cours."""
        race_id = params.get('race_id') or self.race.get_current_race_id()
        timestamp = datetime.now().isoformat(' ', 'microseconds')
        query = '''
        INSERT INTO sensors_data (
            timestamp, strain_gage_1, strain_gage_2, strain_gage_3, strain_gage_4, strain_gage_5,
            strain_gage_6, strain_gage_7, strain_gage_8, strain_gage_9, strain_gage_10,
            strain_gage_11, strain_gage_12, strain_gage_13, strain_gage_14, strain_gage_15,
            strain_gage_16, strain_gage_17, strain_gage_18, strain_gage_19, strain_gage_20,
            strain_gage_21, strain_gage_22, strain_gage_23, strain_gage_24, strain_gage_25,
            strain_gage_26, strain_gage_27, strain_gage_28, strain_gage_29, strain_gage_30,
            strain_gage_31, strain_gage_32, strain_gage_33, strain_gage_34, strain_gage_35,
            strain_gage_36, strain_gage_37, strain_gage_38, strain_gage_39, strain_gage_40,
            strain_gage_41, strain_gage_42, strain_gage_43, strain_gage_44, strain_gage_45,
            strain_gage_46, strain_gage_47, strain_gage_48, strain_gage_49, strain_gage_50,
            accelerometer, rpm_counter1, rpm_counter2, speed_counter, race_id,
            accel_1_x, accel_1_y, accel_1_z, accel_1_rot_x, accel_1_rot_y, accel_1_rot_z,
            accel_2_x, accel_2_y, accel_2_z, accel_2_rot_x, accel_2_rot_y, accel_2_rot_z,
            accel_3_x, accel_3_y, accel_3_z, accel_3_rot_x, accel_3_rot_y, accel_3_rot_z,
            accel_4_x, accel_4_y, accel_4_z, accel_4_rot_x, accel_4_rot_y, accel_4_rot_z,
            accel_5_x, accel_5_y, accel_5_z, accel_5_rot_x, accel_5_rot_y, accel_5_rot_z
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                  ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                  ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,
                  ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        '''
        params_tuple = (
            timestamp, params['strain_gage_1'], params['strain_gage_2'], params['strain_gage_3'], params['strain_gage_4'], params['strain_gage_5'],
            params['strain_gage_6'], params['strain_gage_7'], params['strain_gage_8'], params['strain_gage_9'], params['strain_gage_10'],
            params['strain_gage_11'], params['strain_gage_12'], params['strain_gage_13'], params['strain_gage_14'], params['strain_gage_15'],
            params['strain_gage_16'], params['strain_gage_17'], params['strain_gage_18'], params['strain_gage_19'], params['strain_gage_20'],
            params['strain_gage_21'], params['strain_gage_22'], params['strain_gage_23'], params['strain_gage_24'], params['strain_gage_25'],
            params['strain_gage_26'], params['strain_gage_27'], params['strain_gage_28'], params['strain_gage_29'], params['strain_gage_30'],
            params['strain_gage_31'], params['strain_gage_32'], params['strain_gage_33'], params['strain_gage_34'], params['strain_gage_35'],
            params['strain_gage_36'], params['strain_gage_37'], params['strain_gage_38'], params['strain_gage_39'], params['strain_gage_40'],
            params['strain_gage_41'], params['strain_gage_42'], params['strain_gage_43'], params['strain_gage_44'], params['strain_gage_45'],
            params['strain_gage_46'], params['strain_gage_47'], params['strain_gage_48'], params['strain_gage_49'], params['strain_gage_50'],
            params['accelerometer'], params['rpm_counter1'], params['rpm_counter2'], params['speed_counter'], race_id,
            params['accel_1_x'], params['accel_1_y'], params['accel_1_z'], params['accel_1_rot_x'], params['accel_1_rot_y'], params['accel_1_rot_z'],
            params['accel_2_x'], params['accel_2_y'], params['accel_2_z'], params['accel_2_rot_x'], params['accel_2_rot_y'], params['accel_2_rot_z'],
            params['accel_3_x'], params['accel_3_y'], params['accel_3_z'], params['accel_3_rot_x'], params['accel_3_rot_y'], params['accel_3_rot_z'],
            params['accel_4_x'], params['accel_4_y'], params['accel_4_z'], params['accel_4_rot_x'], params['accel_4_rot_y'], params['accel_4_rot_z'],
            params['accel_5_x'], params['accel_5_y'], params['accel_5_z'], params['accel_5_rot_x'], params['accel_5_rot_y'], params['accel_5_rot_z']
        )
        self.db.execute_query(query, params_tuple)
        print(f"Données insérées avec un horodatage précis : {timestamp}")