# microservicio_carga_documento/routes.py
from flask import request, jsonify, Blueprint
from common.firebase_utils import get_firestore_instance

carga_documento_bp = Blueprint('carga_documento', __name__)

@carga_documento_bp.route('/cargar_documento', methods=['POST'])
def cargar_documento():
    try:
        # Obtener datos de la solicitud
        data = request.get_json()

        # Verificar la autenticación y autorización del usuario, por ejemplo, utilizando Firebase Authentication
        # Esto depende de tu sistema de autenticación y seguridad

        # Conectar con Firebase Firestore
        firestore = get_firestore_instance()

        # Obtener información del documento enviado
        nombre_documento = data['nombre']
        contenido_documento = data['contenido']
        tipo_documento = data['tipo']

        # Realizar las operaciones de carga y almacenamiento del documento
        # Por ejemplo, puedes guardar el documento en una colección de Firebase Firestore
        documento_ref = firestore.collection('documentos').add({
            'nombre': nombre_documento,
            'contenido': contenido_documento,
            'tipo': tipo_documento
        })

        return jsonify({'message': 'Documento cargado exitosamente', 'documento_id': documento_ref.id}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Otras rutas relacionadas con la carga de documentos pueden ir aquí


