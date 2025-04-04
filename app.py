from flask import Flask, request, jsonify, send_from_directory, make_response
import sqlite3
from datetime import datetime
import uuid

app = Flask(__name__, static_folder='dist')
DATABASE = "data/garbage_collection.db"

def query_db(query, args=(), one=False):
    """Helper function to query the database."""
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(query, args)
    rv = cur.fetchall()
    conn.commit()
    conn.close()
    return (rv[0] if rv else None) if one else rv


@app.before_request
def set_device_id():
    if 'device_id' not in request.cookies:
        resp = make_response()
        resp.set_cookie('device_id', str(uuid.uuid4()))
        return resp


@app.route('/')
def serve_index():
    return send_from_directory('dist', 'index.html')

@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('dist', path)

@app.route('/get_last_collection', methods=['GET'])
def get_last_collection():
    street_id = request.args.get('street_id')
    if not street_id:
        return jsonify({"error": "street_id is required"}), 400

    result = query_db(
        "SELECT MAX(timestamp) AS last_collected FROM garbage_collection WHERE street_id = ?",
        [street_id],
        one=True
    )
    if result and result["last_collected"]:
        return jsonify({"street_id": street_id, "last_collected": result["last_collected"]})
    else:
        return jsonify({"error": "No collection data found for the given street"}), 404

@app.route('/request_collection', methods=['POST'])
def request_collection():
    """Request garbage collection for a street."""
    data = request.get_json()
    street_id = data.get('street_id')
    garbage_type = data.get('garbage_type')
    state = int(data.get('state'))
    device_id = request.cookies.get('device_id')
    ip = request.remote_addr

    if not street_id or not garbage_type:
        return jsonify({"error": "street_id, garbage_type are required"}), 400

    query_db(
        """
        INSERT INTO user_request (latitude, longitude, street_id, garbage_type, state, device_id, ip)
        VALUES (NULL, NULL, ?, ?, ?, ?, ?)
        """,
        [street_id, garbage_type, state, device_id, ip]
    )
    return jsonify({"message": "Collection request submitted successfully"}), 201

@app.route('/confirm_collection', methods=['POST'])
def confirm_collection():
    """Confirm that garbage collection has occurred."""
    data = request.get_json()
    street_id = data.get('street_id')
    garbage_type = data.get('garbage_type')

    if not street_id or not garbage_type:
        return jsonify({"error": "street_id and garbage_type are required"}), 400

    query_db(
        """
        INSERT INTO garbage_collection (garbage_type, street_id, timestamp)
        VALUES (?, ?, ?)
        """,
        [garbage_type, street_id, datetime.now()]
    )
    return jsonify({"message": "Collection confirmed successfully"}), 200
@app.route('/street_garbage_status', methods=['GET'])
def get_street_garbage_status():
    results = query_db("SELECT * FROM street_garbage_status")
    return jsonify([dict(row) for row in results])

@app.route('/city_part_garbage_status', methods=['GET'])
def get_city_part_garbage_status():
    results = query_db("SELECT * FROM city_part_garbage_status")
    return jsonify([dict(row) for row in results])
if __name__ == '__main__':
    app.run(debug=True)