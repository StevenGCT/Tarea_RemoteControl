from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

# Función para obtener el estado actual
def get_status():
    # Código para obtener el estado actual del sistema
    # Devuelve un diccionario con los datos de estado
    return {
        'cpu': 30,
        'ram': 50,
        'hard_disk': 80
    }

# Función para actualizar el estado y emitir un mensaje de socket a los clientes conectados
def update_status():
    status = get_status()
    socketio.emit('status_update', status)

# Ruta inicial para servir el dashboard
@app.route('/')
def index():
    return render_template('index.html')

# Función que se ejecuta cuando un cliente se conecta
@socketio.on('connect')
def on_connect():
    # Enviar el estado actual al cliente que se conecta
    status = get_status()
    socketio.emit('status_update', status)

# Función que se ejecuta cuando un cliente se desconecta
@socketio.on('disconnect')
def on_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    # Configurar una tarea de actualización de estado para que se ejecute cada 5 segundos
    update_status_interval = 5
    socketio.start_background_task(update_status, interval=update_status_interval)

    # Iniciar el servidor Flask-SocketIO
    socketio.run(app)