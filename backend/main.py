# main.py
from flask_cors import CORS
from src import create_app
from flask_socketio import SocketIO
app = create_app("dev")
CORS(app)
socketio = SocketIO(app)

if __name__ == '__main__':
	socketio.run(app)
