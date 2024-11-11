from flask import Flask, render_template, jsonify
import platform
import psutil
import socket
import json
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/server-info')
def get_server_info():
    server_info = {
        'system': platform.system(),
        'release': platform.release(),
        'version': platform.version(),
        'machine': platform.machine(),
        'processor': platform.processor(),
        'hostname': socket.gethostname(),
        'cpu_cores': psutil.cpu_count(),
        'cpu_usage': psutil.cpu_percent(interval=1),
        'memory_total': round(psutil.virtual_memory().total / (1024 ** 3), 2),  # GB
        'memory_available': round(psutil.virtual_memory().available / (1024 ** 3), 2),  # GB
        'timestamp': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    return jsonify(server_info)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
