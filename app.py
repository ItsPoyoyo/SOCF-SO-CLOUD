from flask import Flask, render_template
import platform
import psutil
import os
import json


names = "Hussein Ali El Gazouini, Hassan Ali El Gazouini"

x_names = {
    "name1": "Hussein Ali El Gazouini",
    "name2": "Hassan Ali El Gazouini",
    "name3": "Murilo Zimerman Fortaleza ",
}

# get OS information
print("System Information:")
print(f"System: {platform.platform()}")

# get PID
print(os.getpid())

# get CPU usage
print(f"CPU Usage: {psutil.cpu_percent(interval=1)}%")

#get Memory usage
memory = psutil.virtual_memory().used // 1024 ** 2
print(f"Memory Usage: {memory} MB")

APP:app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/info')
def info():
    return json.dumps(x_names, indent=4)

@app.route('/metricas')
def get_metrics():

    metrics = {
        'Nome': names,
        'Operating System': platform.platform(),
        'Process ID': os.getpid(),
        'CPU Usage (%)': psutil.cpu_percent(interval=1),
        'Memory Usage (MB)': memory
    }

    return json.dumps(metrics, indent=4)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)), debug=True)