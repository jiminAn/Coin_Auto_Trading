# main.py
from flask_cors import  CORS

from backend.src import create_app

app = create_app("dev")
CORS(app)

if __name__ == '__main__':
	import configparser

	config = configparser.ConfigParser()
	app.run(host='127.0.0.1', port=5000, debug=True)
