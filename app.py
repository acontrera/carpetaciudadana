from fastapi import FastAPI, HTTPException, APIRouter, Depends, Form
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from starlette.requests import Request
from pydantic import BaseModel
import firebase_admin
from firebase_admin import credentials, auth, db, exceptions

# Inicializa Firebase Admin SDK
try:
    cred = credentials.Certificate("common/capetaciudadana-firebase-adminsdk-lwsjg-9f93150542.json")
    firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://capetaciudadana-default-rtdb.firebaseio.com/'  # Reemplaza esto con la URL de tu base de datos
})
    print("Firebase se ha inicializado correctamente")
except Exception as e:
    print(f"Error en la inicialización de Firebase: {str(e)}")

# Define el enrutador autenticacion_bp
autenticacion_bp = APIRouter()

app = FastAPI()

class UserLogin(BaseModel):
    email: str
    password: str


@autenticacion_bp.post('/registro', status_code=200)
async def registro(user_login: UserLogin):
    try:
        email = user_login.email
        password = user_login.password

        # Comprueba si el usuario ya existe en Firebase
        try:
            user = auth.get_user_by_email(email)
            return JSONResponse(content={"message": "El correo electrónico ya está registrado"}, status_code=400)
        except exceptions.NotFoundError:
            # El usuario no existe, así que continuamos con el registro
            pass
        
        # Registra al usuario en Firebase Authentication
        user = auth.create_user(
            email=email,
            password=password
        )
        
        # Crea una instancia de Usuario para almacenar en la base de datos si es necesario
        nuevo_usuario = {
            "email": email,
            "password": password,
            # Otras propiedades del usuario si es necesario
        }

        # Intenta guardar el registro del usuario en Firebase Realtime Database
        try:
            db.reference('/usuarios').push(nuevo_usuario)
            return {"message": "Registro exitoso"}
        except exceptions.FirebaseError as db_error:
            return JSONResponse(content={"message": f"Error al guardar en Firebase: {str(db_error)}"}, status_code=400)
    
    except exceptions.FirebaseError as auth_error:
        if "No user record found" in str(auth_error):
            return JSONResponse(content={"message": f"Error en el registro: {str(auth_error)}"}, status_code=400)



@autenticacion_bp.get('/registro')
async def mostrar_formulario_registro(request: Request):
    return templates.TemplateResponse("registro.html", {"request": request})

@autenticacion_bp.get('/login')
async def mostrar_formulario_login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@autenticacion_bp.post('/login', response_model=dict)
async def login(user_login: UserLogin = Depends(UserLogin)):
    try:
       
        email = user_login.email
        password = user_login.password

        user = auth.get_user_by_email(email)

       # Verifica la contraseña del usuario
        auth.update_user(user.uid, password=password)
        print("Recibida solicitud POST en /autenticacion/login")
        print(f"Datos recibidos: email={user_login.email}, password={user_login.password}")

        if not user:
            raise HTTPException(status_code=400, detail='Usuario no encontrado')

        # Verifica la contraseña del usuario
        
        # Esto podría requerir una lógica adicional para comparar la contraseña proporcionada con la almacenada en Firebase.
        # Puedes utilizar la autenticación personalizada para manejar esta lógica.
        # https://firebase.google.com/docs/auth/admin/manage-users#set_a_password
        # A continuación, se muestra un ejemplo simplificado, pero te recomiendo consultar la documentación para implementarla de manera segura.
        custom_token = auth.create_custom_token(user.uid)

        return {'message': 'Inicio de sesión exitoso', 'custom_token': custom_token}

    except exceptions.FirebaseError as e:
        raise HTTPException(status_code=400, detail='Error de autenticación: ' + str(e))


# Configura la ubicación de los archivos estáticos
app.mount("/static", StaticFiles(directory="microservicio_autenticacion/static"), name="static")

# Configura la ubicación de las plantillas
templates = Jinja2Templates(directory="microservicio_autenticacion/templates")

# Define la ruta para la página de inicio
@app.get("/")
async def home(request: Request):
    return templates.TemplateResponse("registro.html", {"request": request})

# Incluye el enrutador autenticacion_bp en la aplicación principal
app.include_router(autenticacion_bp, prefix="/autenticacion", tags=["Authentication"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
