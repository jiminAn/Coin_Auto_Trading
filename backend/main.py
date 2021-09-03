# main.py
from flask_cors import  CORS
from src import create_app
app = create_app("dev")
CORS(app)

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000, debug=True)
