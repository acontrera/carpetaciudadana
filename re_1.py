import requests

# URL de la API a la que deseas hacer la solicitud POST
url = 'http://127.0.0.1:8000/autenticacion/registro'

# Datos que deseas enviar en el cuerpo de la solicitud en formato JSON
data = {
    "email": "ingsisacontreras12@gmail.com",
    "password": "123456"
}

# Realiza la solicitud POST enviando los datos en el cuerpo como JSON
response = requests.post(url, json=data)

# Verifica la respuesta
if response.status_code == 200:
    print('Solicitud exitosa:', response.json())
else:
    print('Error en la solicitud:', response.status_code, response.text)
