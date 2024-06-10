from flask import Flask, render_template, jsonify, request, send_file
import Main

app = Flask(
    __name__,
    template_folder='www/templates',
    static_folder='www/static'
)

# Variable globale pour simuler l'état du serveur
is_running = False

@app.route('/init')
def init_route():
    Main.initDB()
    return 'init trig'

@app.route('/creat')
def creat_route():
    Main.db.creatTable()
    return jsonify(result="Part 2 reset successfully")

@app.route('/delete-all-tables')
def delete_all_tables_route():
    Main.db.delete_all_tables()
    return jsonify(result="Part 1 reset successfully")

@app.route('/add-entre')
def add_user_route():
    Main.add_donne(9, 43, 9, 3, 6)
    return 'une entrée ajoutée'

@app.route('/get-all')
def get_all_route():
    print(Main.get_all_donne())
    return Main.get_all_donne()

@app.route('/get-all-json')
def get_all_json_route():
    print(Main.get_all_donne_json())
    return Main.get_all_donne_json()

@app.route('/Start')
def start_route():
    if not Main.course.RecordState:
        Main.course.RecordState = True
        Main.course.start_race()
    return jsonify(result="Update started successfully")

@app.route('/Stop')
def stop_route():
    if Main.course.RecordState:
        Main.course.RecordState = False
        Main.course.end_race()
    return jsonify(result="Update stopped successfully")

@app.route('/get-state')
def get_state_route():
    state = "Running" if Main.course.RecordState else "Stopped"
    return jsonify(state=state)

@app.route('/')
def web_page_route():
    return render_template('index.html')

@app.route('/get-data')
def get_data():
    data = Main.db.get_data_last_5_minutes()
    if data is None:
        return jsonify(data=[]), 200  # Assurez-vous de renvoyer une liste vide si aucune donnée n'est trouvée
    return jsonify(data=data)

@app.route('/get-RPM1-5min')
def get_RPM1_5min():
    img = Main.basicGraph.getGraphRPM1_5min()
    return send_file(img, mimetype='image/png')

@app.route('/get-RPM2-5min')
def get_RPM2_5min():
    img = Main.basicGraph.getGraphRPM2_5min()
    return send_file(img, mimetype='image/png')

@app.route('/get-strain_gage-5min')
def get_strain_gage_5min():
    img = Main.basicGraph.getGraphstrain_gage_5min()
    return send_file(img, mimetype='image/png')



@app.route('/add-data', methods=['PUT'])
def add_data_route():
    print("add-data route")
    if Main.course.RecordState:
        data = request.get_json()
        if not data:
            return jsonify(error="Invalid JSON"), 400

        # Initialiser les paramètres avec leurs valeurs par défaut
        params = {
            'strain_gage_1': 0, 'strain_gage_2': 0, 'strain_gage_3': 0, 'strain_gage_4': 0, 'strain_gage_5': 0,
            'strain_gage_6': 0, 'strain_gage_7': 0, 'strain_gage_8': 0, 'strain_gage_9': 0, 'strain_gage_10': 0,
            'strain_gage_11': 0, 'strain_gage_12': 0, 'strain_gage_13': 0, 'strain_gage_14': 0, 'strain_gage_15': 0,
            'strain_gage_16': 0, 'strain_gage_17': 0, 'strain_gage_18': 0, 'strain_gage_19': 0, 'strain_gage_20': 0,
            'strain_gage_21': 0, 'strain_gage_22': 0, 'strain_gage_23': 0, 'strain_gage_24': 0, 'strain_gage_25': 0,
            'strain_gage_26': 0, 'strain_gage_27': 0, 'strain_gage_28': 0, 'strain_gage_29': 0, 'strain_gage_30': 0,
            'strain_gage_31': 0, 'strain_gage_32': 0, 'strain_gage_33': 0, 'strain_gage_34': 0, 'strain_gage_35': 0,
            'strain_gage_36': 0, 'strain_gage_37': 0, 'strain_gage_38': 0, 'strain_gage_39': 0, 'strain_gage_40': 0,
            'strain_gage_41': 0, 'strain_gage_42': 0, 'strain_gage_43': 0, 'strain_gage_44': 0, 'strain_gage_45': 0,
            'strain_gage_46': 0, 'strain_gage_47': 0, 'strain_gage_48': 0, 'strain_gage_49': 0, 'strain_gage_50': 0,
            'accelerometer': 0, 'rpm_counter1': 0, 'rpm_counter2': 0, 'speed_counter': 0, 'race_id': None,
            'accel_1_x': 0, 'accel_1_y': 0, 'accel_1_z': 0, 'accel_1_rot_x': 0, 'accel_1_rot_y': 0, 'accel_1_rot_z': 0,
            'accel_2_x': 0, 'accel_2_y': 0, 'accel_2_z': 0, 'accel_2_rot_x': 0, 'accel_2_rot_y': 0, 'accel_2_rot_z': 0,
            'accel_3_x': 0, 'accel_3_y': 0, 'accel_3_z': 0, 'accel_3_rot_x': 0, 'accel_3_rot_y': 0, 'accel_3_rot_z': 0,
            'accel_4_x': 0, 'accel_4_y': 0, 'accel_4_z': 0, 'accel_4_rot_x': 0, 'accel_4_rot_y': 0, 'accel_4_rot_z': 0,
            'accel_5_x': 0, 'accel_5_y': 0, 'accel_5_z': 0, 'accel_5_rot_x': 0, 'accel_5_rot_y': 0, 'accel_5_rot_z': 0
        }

        # Mettre à jour les paramètres uniquement si les clés sont présentes dans la requête JSON
        for key in data:
            if key in params:
                params[key] = data[key]

        try:
            # Appel de la méthode d'insertion avec les paramètres extraits
            Main.data.insert_sensor_data(params)
            return jsonify(result="Data added successfully"), 201
        except Exception as e:
            return jsonify(error=str(e)), 500

    return jsonify(result="RecordState est a off"), 201

@app.route('/get-last-strain-gage/<int:strain_gage_id>', methods=['GET'])
def get_last_strain_gage(strain_gage_id):
    try:
        result = Main.db.getLasvalueStaing(strain_gage_id)
        return jsonify(result), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/get-last-imu-g/<int:strain_gage_id>', methods=['GET'])
def get_last_imu_g(strain_gage_id):
    try:
        result = Main.db.getLasvalueAccelerationsG(strain_gage_id)
        return jsonify(result), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
