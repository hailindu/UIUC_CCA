from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods=['POST'])
def stress_cpu():
    # Start the stress_cpu.py script as a separate process
    subprocess.Popen(["python3", "stress_cpu.py"])
    return 'CPU stress test started', 200

@app.route('/', methods=['GET'])
def home():
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)
    return private_ip

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)