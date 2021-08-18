# main.py
from src import create_app
#from src.model.models import User
app = create_app("dev")

if __name__ == '__main__':
	app.run()