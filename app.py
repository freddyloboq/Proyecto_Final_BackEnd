from flask import Flask, jsonify, request, json
from flask_mysqldb import MySQL
from flask_cors import CORS
from datetime import datetime

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'bb1xxu9nma9q0hp03dbj-mysql.services.clever-cloud.com'
app.config['MYSQL_USER'] = 'u5mdumqultlzvi5z'
app.config['MYSQL_PASSWORD'] = 'lTL2C898HPYXUUZJxFJX'
app.config['MYSQL_DB'] = 'bb1xxu9nma9q0hp03dbj'

mysql = MySQL(app)
CORS(app)


###################################################################################
#           method POST para ADD
###################################################################################
@app.route('/api/container/add_container', methods=['POST'])
def containersPost():
    cur = mysql.connection.cursor()
    typeOfMaterial = request.get_json()['typeOfMaterial']
    capacity = request.get_json()['capacity']
    location = request.get_json()['location']
    length = request.get_json()['length']
    latitude = request.get_json()['latitude']
    registerDate = datetime.utcnow()

    cur.execute("INSERT INTO container (typeOfMaterial, capacity, location, length, latitude, registerDate) VALUES ('" +
                str(typeOfMaterial) + "', '" +
                str(capacity) + "', '" +
                str(location) + "', '" +
                str(length) + "', '" +
                str(latitude) + "', '" +
                str(registerDate) + "')")
    mysql.connection.commit()

    result = {
        'typeOfMaterial': typeOfMaterial,
        'capacity': capacity,
        'location': location,
        'length': length,
        'latitude': latitude,
        'registerDate': registerDate
    }

    return jsonify({'result': result})


###################################################################################
#           method PUT para EDIT
###################################################################################
# @app.route('/api/container/edit_container/<int:id>', methods=['GET'])
# def containersEdit(id):
#     # cur = mysql.connection.cursor()
#     # typeOfMaterial = request.get_json()['typeOfMaterial']
#     # capacity = request.get_json()['capacity']
#     # location = request.get_json()['location']
#     # length = request.get_json()['length']
#     # latitude = request.get_json()['latitude']
#     # registerDate = datetime.utcnow()

#     cur.execute("SELECT * FROM container WHERE containerId=%s", (id,))
#     # row_headers = [x[0]
#     #                for x in cur.description]  # this will extract row headers
#     # dataContainer = cur.fetchall()
#     # json_data = []

#     # for result in dataContainer:
#     #     json_data.append(dict(zip(row_headers, result)))

#     # result = {
#     #     'typeOfMaterial': typeOfMaterial,
#     #     'capacity': capacity,
#     #     'location': location,
#     #     'length': length,
#     #     'latitude': latitude,
#     #     'registerDate': registerDate
#     # }

#     return jsonify({'id': id})
#     # return jsonify({'result': result})


###################################################################################
#           method PUT para UPDATE
###################################################################################
@app.route('/api/container/update_container/<int:id>', methods=['PUT'])
def containersUpdate(id):
    if request.method == 'PUT':
        cur = mysql.connection.cursor()
        typeOfMaterial = request.get_json()['typeOfMaterial']
        capacity = request.get_json()['capacity']
        location = request.get_json()['location']
        length = request.get_json()['length']
        latitude = request.get_json()['latitude']
        registerDate = datetime.utcnow()

        cur.execute("""
                UPDATE container
                SET typeOfMaterial = %s,
                    capacity = %s,
                    location = %s,
                    length = %s,
                    latitude = %s
                WHERE containerId=%s
            """, (typeOfMaterial, capacity, location, length, latitude, id,))

        mysql.connection.commit()

        result = {
            'typeOfMaterial': typeOfMaterial,
            'capacity': capacity,
            'location': location,
            'length': length,
            'latitude': latitude,
            'registerDate': registerDate
        }

    return jsonify({'result': result})

###################################################################################
#           method GET para GET
###################################################################################


@app.route('/api/container', methods=['GET'])
def containersGet():

    cur = mysql.connection.cursor()

    cur.execute("SELECT * FROM container")
    row_headers = [x[0]
                   for x in cur.description]  # this will extract row headers
    dataContainer = cur.fetchall()
    json_data = []

    for result in dataContainer:
        json_data.append(dict(zip(row_headers, result)))
    # dataJson = json.dumps(json_data)

    return jsonify(json_data)
    # return jsonify(dataJson)


###################################################################################
#           method DELETE
###################################################################################
@app.route('/api/container/delete_container/<int:id>', methods=['DELETE'])
def containersDelete(id):
    cur = mysql.connection.cursor()
    # typeOfMaterial = request.get_json()['typeOfMaterial']
    # capacity = request.get_json()['capacity']
    # location = request.get_json()['location']
    # length = request.get_json()['length']
    # latitude = request.get_json()['latitude']
    # registerDate = datetime.utcnow()

    cur.execute('DELETE FROM container WHERE containerId=%s', (id,))
    mysql.connection.commit()

    # result = {
    #     'typeOfMaterial': typeOfMaterial,
    #     'capacity': capacity,
    #     'location': location,
    #     'length': length,
    #     'latitude': latitude,
    #     'registerDate': registerDate
    # }
    print(id)
    return jsonify({"id": id})
    # jsonify({'result': result})


###########################################
## ------- SESION NOTIFICACIONES ------- ##
###########################################
# GET
@app.route('/api/get_notification', methods=['GET'])
def get_notification():
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM notification")
    row_headers = [x[0]
                   for x in cur.description]  # this will extract row headers
    dataNotification = cur.fetchall()
    json_data = []
    for result in dataNotification:
        json_data.append(dict(zip(row_headers, result)))
    return jsonify(json_data)
# POST


@app.route('/api/create_notification', methods=['POST'])
def create_notification():
    cur = mysql.connection.cursor()
    status = request.get_json()['status']
    notify = request.get_json()['notify']
    notificationdate = datetime.utcnow()
    cur.execute("INSERT INTO notification (status, notify, notificationdate) VALUES ('" +
                str(status) + "', '" +
                str(notify) + "', '" +
                str(notificationdate) + "')")
    mysql.connection.commit()
    result = {
        'status': status,
        'notify': notify,
        'notificationdate': notificationdate
    }
    return jsonify({'result': result})


if __name__ == '__main__':
    app.run(debug=True)
