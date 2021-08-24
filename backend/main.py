# main.py
from src import create_app
app = create_app("dev")

if __name__ == '__main__':
	app.run(host='127.0.0.1', port=5000, debug=True)