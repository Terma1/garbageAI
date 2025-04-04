from flask import Flask, request, jsonify, render_template
import sqlite3
from datetime import datetime

app = Flask(__name__)
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

@app.route('/')
def index():
    return render_template('index.html')


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
    ip = request.remote_addr

    if not street_id or not garbage_type:
        return jsonify({"error": "street_id, garbage_type are required"}), 400

    query_db(
        """
        INSERT INTO user_request (latitude, longitude, street_id, garbage_type, state, device_id, ip)
        VALUES (NULL, NULL, ?, ?, ?, ?, ?)
        """,
        [street_id, garbage_type, state, 0, ip] 
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

if __name__ == '__main__':
    app.run(debug=True)