from flask import Blueprint, request, jsonify
from common.firebase_utils import get_firebase_db

solicitud_documento_bp = Blueprint('solicitud_documento', __name__)

# Ruta para registrar una solicitud de documento
@solicitud_documento_bp.route('/registrar_solicitud', methods=['POST'])
def registrar_solicitud():
    try:
        # Obtener datos de la solicitud desde la solicitud
        data = request.get_json()
        ciudadano_id = data['ciudadano_id']
        entidad_id = data['entidad_id']
        tipo_documento = data['tipo_documento']

        # Realizar la lógica para registrar la solicitud en la base de datos
        db = get_firebase_db()

        # Aquí puedes agregar la lógica para registrar la solicitud en la base de datos
        # Esto puede implicar crear un nuevo registro en una colección de solicitudes
        
        # Devolver una respuesta exitosa
        return jsonify({'message': 'Solicitud registrada exitosamente'}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Otras rutas relacionadas con la solicitud de documentos pueden ir aquí
