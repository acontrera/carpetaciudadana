import firebase_admin
from firebase_admin import credentials, firestore

# Define la ruta al archivo JSON de configuración de Firebase Admin SDK.
FIREBASE_CREDENTIALS_PATH = "D:\carpeta_ciudadana\capetaciudadana-firebase-adminsdk-lwsjg-9f93150542.json"

# Variable para almacenar la instancia de la aplicación Firebase Admin SDK
_firebase_app = None

# Función para inicializar Firebase Admin SDK
def initialize_firebase_app():
    try:
        # Evita inicializar Firebase si ya está inicializado
        global _firebase_app
        if not _firebase_app:
            cred = credentials.Certificate(FIREBASE_CREDENTIALS_PATH)
            _firebase_app = firebase_admin.initialize_app(cred)

        # Retorna la instancia de Firestore desde la aplicación Firebase Admin SDK
        return _firebase_app

    except Exception as e:
        raise Exception("Error al inicializar Firebase: " + str(e))

# Función para obtener una instancia de Firestore
def get_firestore_instance():
    # Inicializa la aplicación Firebase Admin SDK si no está inicializada
    initialize_firebase_app()

    # Obtiene y retorna la instancia de Firestore desde la aplicación Firebase Admin SDK
    return firestore.client()

# También puedes agregar funciones para obtener otras instancias de Firebase si es necesario
# Por ejemplo, una función para obtener la instancia de autenticación de Firebase
def get_firebase_auth():
    # Inicializa la aplicación Firebase Admin SDK si no está inicializada
    initialize_firebase_app()

    # Retorna la instancia de autenticación de Firebase
    return firebase_admin.auth()

# Otra función para obtener la instancia de la base de datos de Firebase
def get_firebase_db():
    # Inicializa la aplicación Firebase Admin SDK si no está inicializada
    initialize_firebase_app()

    # Retorna la instancia de la base de datos de Firebase
    return firebase_admin.db()
