from datetime import datetime

class donne():
    db = None
    race = None

    def __init__(self, DB, Race):
        self.db = DB
        self.race = Race

    def insert_sensor_data(self, strain_gage_1=0, strain_gage_2=0, strain_gage_3=0, strain_gage_4=0, strain_gage_5=0,
                           strain_gage_6=0, strain_gage_7=0, strain_gage_8=0, strain_gage_9=0, strain_gage_10=0,
                           strain_gage_11=0, strain_gage_12=0, strain_gage_13=0, strain_gage_14=0, strain_gage_15=0,
                           strain_gage_16=0, strain_gage_17=0, strain_gage_18=0, strain_gage_19=0, strain_gage_20=0,
                           strain_gage_21=0, strain_gage_22=0, strain_gage_23=0, strain_gage_24=0, strain_gage_25=0,
                           strain_gage_26=0, strain_gage_27=0, strain_gage_28=0, strain_gage_29=0, strain_gage_30=0,
                           strain_gage_31=0, strain_gage_32=0, strain_gage_33=0, strain_gage_34=0, strain_gage_35=0,
                           strain_gage_36=0, strain_gage_37=0, strain_gage_38=0, strain_gage_39=0, strain_gage_40=0,
                           strain_gage_41=0, strain_gage_42=0, strain_gage_43=0, strain_gage_44=0, strain_gage_45=0,
                           strain_gage_46=0, strain_gage_47=0, strain_gage_48=0, strain_gage_49=0, strain_gage_50=0,
                           accelerometer=0, rpm_counter1=0, rpm_counter2=0, speed_counter=0, race_id=None,
                           accel_1_x=0, accel_1_y=0, accel_1_z=0, accel_1_rot_x=0, accel_1_rot_y=0, accel_1_rot_z=0,
                           accel_2_x=0, accel_2_y=0, accel_2_z=0, accel_2_rot_x=0, accel_2_rot_y=0, accel_2_rot_z=0,
                           accel_3_x=0, accel_3_y=0, accel_3_z=0, accel_3_rot_x=0, accel_3_rot_y=0, accel_3_rot_z=0,
                           accel_4_x=0, accel_4_y=0, accel_4_z=0, accel_4_rot_x=0, accel_4_rot_y=0, accel_4_rot_z=0,
                           accel_5_x=0, accel_5_y=0, accel_5_z=0, accel_5_rot_x=0, accel_5_rot_y=0, accel_5_rot_z=0):
        """Insère des données dans la table sensors_data avec l'ID de la course en cours."""
        if race_id is None:
            race_id = self.race.get_current_race_id()
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
        params = (timestamp, strain_gage_1, strain_gage_2, strain_gage_3, strain_gage_4, strain_gage_5,
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
                  accel_5_x, accel_5_y, accel_5_z, accel_5_rot_x, accel_5_rot_y, accel_5_rot_z)
        self.db.execute_query(query, params)
        print(f"Données insérées avec un horodatage précis : {timestamp}")