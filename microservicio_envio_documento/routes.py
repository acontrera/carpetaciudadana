# microservicio_envio_documento/routes.py
from flask import request, jsonify, Blueprint
from common.firebase_utils import get_firestore_instance

envio_documento_bp = Blueprint('envio_documento', __name__)

@envio_documento_bp.route('/enviar_documento', methods=['POST'])
def enviar_documento():
    try:
        # Obtener datos de la solicitud
        data = request.get_json()

        # Verificar la autenticación y autorización del usuario, por ejemplo, utilizando Firebase Authentication
        # Esto depende de tu sistema de autenticación y seguridad

        # Conectar con Firebase Firestore
        firestore = get_firestore_instance()

        # Obtener información sobre el envío del documento
        destinatario = data['destinatario']
        tipo_documento = data['tipo']
        contenido_documento = data['contenido']

        # Realizar el envío del documento, por ejemplo, almacenarlo en una colección de Firestore
        documento_ref = firestore.collection('documentos_enviados').add({
            'destinatario': destinatario,
            'tipo': tipo_documento,
            'contenido': contenido_documento,
            'estado': 'Enviado'  # Puedes agregar más detalles de seguimiento del estado del envío
        })

        return jsonify({'message': 'Documento enviado exitosamente', 'documento_id': documento_ref.id}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Otras rutas relacionadas con el envío de documentos pueden ir aquí
