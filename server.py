# server.py
from flask import Flask, jsonify
import datetime

app = Flask(__name__)

@app.route('/time', methods=['GET'])
def get_time():
    # Devuelve el tiempo actual en formato ISO
    current_time = datetime.datetime.now()
    return jsonify({"server_time": current_time.isoformat()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
