from flask import Blueprint, jsonify, request, render_template
from llm_service import call_llm_api, get_models

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
    model = request.json.get("model", "gemma-3-12b-it-IQ4_XS") # Usamos el modelo del request o uno por defecto

    # Cuerpo de la petición
    data = {
        # "model": "openai/gpt-oss-20b", # Asegúrate que este modelo esté disponible en Jan
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": "Eres un asistente útil que siempre responde en español, sin importar el idioma del usuario."
            },
            {"role": "user", "content": prompt}
        ]
    }

    # Llamamos a la función de nuestro servicio
    response_data, status_code = call_llm_api(data)
    return jsonify(response_data), status_code

@chat_bp.route("/ask-image", methods=['GET', 'POST'])
def ask_model_image():
    
    # Obtenemos el prompt del cuerpo JSON de la petición
    prompt = request.json.get("prompt", "Describe this image.")
    model = request.json.get("model", "gemma-3-12b-it-IQ4_XS") # Usamos el modelo del request o uno por defecto
    image_url = request.json.get("image_url") # Recibimos la URL de la imagen (data URL)

    if not image_url:
        return jsonify({"error": "No se proporcionó una URL de imagen (image_url)."}), 400

    data = {
        "model": model, # Asegúrate de usar un modelo multimodal
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    #  {"type": "image_url", "image_url": {"url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Cat_paw.jpg/800px-Cat_paw.jpg"}} # por URL
                    {"type": "image_url", "image_url": {"url": image_url}} # para analizar, solamente funciona por Jan IA
                    # {"type": "image_url", "image_url": image_url} # estandar pero no funciona en LM Studio ni en Jan IA
                ]
            }
        ]
    }
    # Reutilizamos la misma función de servicio
    response_data, status_code = call_llm_api(data)
    return jsonify(response_data), status_code

@chat_bp.route("/models", methods=['GET'])
def list_models():
    """
    Endpoint para obtener la lista de modelos disponibles desde Jan.AI.
    """
    # Llamamos a la función de nuestro servicio para obtener los modelos
    response_data, status_code = get_models()
    
    return jsonify(response_data), status_code


