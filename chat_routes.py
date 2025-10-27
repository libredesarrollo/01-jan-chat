from flask import Blueprint, jsonify, request, render_template
from llm_service import call_jan_api

# Creamos un Blueprint. El primer argumento es el nombre del blueprint,
# y el segundo es el nombre del módulo o paquete, que Flask usa para localizar recursos.
chat_bp = Blueprint('chat_bp', __name__, template_folder='../templates')

@chat_bp.route("/ask", methods=['GET', 'POST'])
def ask_model():
    if request.method == 'GET':
        # Renderiza el formulario. Flask buscará en la carpeta 'templates'
        # relativa a la ubicación del blueprint si se especifica, o en la global.
        return render_template('form.html')

    # Obtenemos el prompt del cuerpo JSON de la petición
    prompt = request.json.get("prompt", "Tell me a joke.")

    # Cuerpo de la petición
    data = {
        "model": "gemma-3-12b-it-IQ4_XS", # Asegúrate que este modelo esté disponible en Jan
        "messages": [
            {"role": "user", "content": prompt}
        ]
    }

    # Llamamos a la función de nuestro servicio
    response_data, status_code = call_jan_api(data)
    return jsonify(response_data), status_code

@chat_bp.route("/ask-image", methods=['GET', 'POST'])
def ask_model_image():
    data = {
        "model": "llava-v1.5-7b-q4", # Asegúrate de usar un modelo multimodal
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this image."},
                    {"type": "image_url", "image_url": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat_paw.jpg/800px-Cat_paw.jpg"}}
                ]
            }
        ]
    }
    # Reutilizamos la misma función de servicio
    response_data, status_code = call_jan_api(data)
    return jsonify(response_data), status_code