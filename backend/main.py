# main.py
from src import create_app
app = create_application("dev")

if __name__ == '__main__':
	app.run()