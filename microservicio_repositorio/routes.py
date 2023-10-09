# microservicio_repositorio/routes.py
from flask import request, jsonify, Blueprint
from common.firebase_utils import get_firestore_instance

repositorio_bp = Blueprint('repositorio', __name__)

@repositorio_bp.route('/documentos', methods=['GET'])
def obtener_documentos():
    try:
        # Obtener datos del usuario autenticado, por ejemplo, utilizando Firebase Authentication
        # Esto depende de tu sistema de autenticación y seguridad

        # Conectar con Firebase Firestore
        firestore = get_firestore_instance()

        # Obtener documentos del usuario desde Firestore
        # Aquí puedes implementar la lógica para recuperar los documentos asociados al usuario autenticado
        # Por ejemplo, si cada usuario tiene una carpeta de documentos en Firestore, puedes consultar esa carpeta
        # y devolver la lista de documentos
        documentos = []

        # Iterar sobre los documentos y recopilar información relevante (nombre, tipo, metadatos, etc.)
        for documento in documentos:
            documentos.append({
                'nombre': documento['nombre'],
                'tipo': documento['tipo'],
                'metadatos': documento['metadatos']
            })

        return jsonify({'documentos': documentos}), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 400

@repositorio_bp.route('/documentos/<documento_id>', methods=['GET'])
def obtener_documento(documento_id):
    try:
        # Obtener datos del usuario autenticado, por ejemplo, utilizando Firebase Authentication
        # Esto depende de tu sistema de autenticación y seguridad

        # Conectar con Firebase Firestore
        firestore = get_firestore_instance()

        # Obtener un documento específico por su ID
        documento = firestore.collection('documentos').document(documento_id).get()

        if documento.exists:
            # Devolver información sobre el documento
            documento_data = documento.to_dict()
            return jsonify({'documento': documento_data}), 200
        else:
            return jsonify({'error': 'Documento no encontrado'}), 404

    except Exception as e:
        return jsonify({'error': str(e)}), 400

# Otras rutas relacionadas con la gestión de documentos pueden ir aquí

