import requests

# Constantes para la configuración de la API LLM Local

LLM_BASE_URL = "http://127.0.0.1:1337/v1"
CHAT_COMPLETIONS_URL = f"{LLM_BASE_URL}/chat/completions"
MODELS_URL = f"{LLM_BASE_URL}/models"

LLM_API_KEY = "12345"  # La clave de autorización, solo para Jan IA, en LM Studio NO hace falta

def call_llm_api(data):
    """
    Realiza una llamada POST a la API de chat LLM Local.

    Args:
        data (dict): El cuerpo de la petición para la API.

    Returns:
        tuple: Una tupla conteniendo la respuesta JSON y el código de estado.
               En caso de error de conexión, devuelve un diccionario de error y 500.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {LLM_API_KEY}"
    }

    try:
        response = requests.post(CHAT_COMPLETIONS_URL, headers=headers, json=data, stream=False)
        response.raise_for_status()  # Lanza una excepción para respuestas 4xx/5xx
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        # Captura errores de conexión, timeouts, etc.
        error_message = {
            "error": f"Error al contactar el servidor LLM Local: {e}",
            "body": str(e)
        }
        return error_message, 500

def get_models():
    """
    Obtiene la lista de modelos disponibles desde la API LLM Local.

    Returns:
        tuple: Una tupla conteniendo la respuesta JSON y el código de estado.
               En caso de error de conexión, devuelve un diccionario de error y 500.
    """
    headers = {
        "Authorization": f"Bearer {LLM_API_KEY}"
    }

    try:
        response = requests.get(MODELS_URL, headers=headers)
        response.raise_for_status()  # Lanza una excepción para respuestas 4xx/5xx
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        # Captura errores de conexión, timeouts, etc.
        error_message = {
            "error": f"Error al contactar el servidor LLM Local: {e}",
            "body": str(e)
        }
        return error_message, 500