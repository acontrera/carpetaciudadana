# microservicio_solicitud_traslado/routes.py
from flask import request, jsonify, Blueprint
from common.firebase_utils import get_firestore_instance

solicitud_traslado_bp = Blueprint('solicitud_traslado', __name__)

@solicitud_traslado_bp.route('/solicitar_traslado', methods=['POST'])
def solicitar_traslado():
    try:
        # Obtener datos del usuario autenticado, por ejemplo, utilizando Firebase Authentication
        # Esto depende de tu sistema de autenticación y seguridad

        # Conectar con Firebase Firestore
        firestore = get_firestore_instance()

        # Obtener datos de la solicitud de traslado enviados en la solicitud JSON
        data = request.get_json()
        usuario_solicitante = data['usuario_solicitante']
        nuevo_operador = data['nuevo_operador']

        # Realizar la lógica para registrar la solicitud de traslado
        # Por ejemplo, puedes crear un registro en Firestore con los datos de la solicitud
        solicitud_traslado_ref = firestore.collection('solicitudes_traslado').add({
            'usuario_solicitante': usuario_solicitante,
            'nuevo_operador': nuevo_operador,
            'estado': 'Pendiente'  # Puedes agregar más detalles de seguimiento del estado de la solicitud
        })

        return jsonify({'message': 'Solicitud de traslado registrada exitosamente', 'solicitud_id': solicitud_traslado_ref.id}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Otras rutas relacionadas con la gestión de solicitudes de traslado pueden ir aquí

