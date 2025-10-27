import requests

# Constantes para la configuración de la API de Jan.AI

API_URL = "http://127.0.0.1:1337/v1/chat/completions"
JAN_API_KEY = "12345"  # La clave de autorización

def call_jan_api(data):
    """
    Realiza una llamada POST a la API de chat de Jan.AI.

    Args:
        data (dict): El cuerpo de la petición para la API.

    Returns:
        tuple: Una tupla conteniendo la respuesta JSON y el código de estado.
               En caso de error de conexión, devuelve un diccionario de error y 500.
    """
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {JAN_API_KEY}"
    }

    try:
        response = requests.post(API_URL, headers=headers, json=data, stream=False)
        response.raise_for_status()  # Lanza una excepción para respuestas 4xx/5xx
        return response.json(), response.status_code
    except requests.exceptions.RequestException as e:
        # Captura errores de conexión, timeouts, etc.
        error_message = {
            "error": f"Error al contactar el servidor de Jan.AI: {e}",
            "body": str(e)
        }
        return error_message, 500