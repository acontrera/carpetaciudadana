# microservicio_autenticacion/app.py
from flask import Flask
from common.firebase_utils import initialize_firebase

app = Flask(__name__)
firebase = initialize_firebase(app)

# Aquí van las rutas definidas en routes.py

if __name__ == '__main__':
    app.run(debug=True)
