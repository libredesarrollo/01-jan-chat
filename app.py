from flask import Flask, redirect, url_for

# Importamos el Blueprint desde nuestro nuevo módulo de rutas
from chat_routes import chat_bp

app = Flask(__name__)

# Registramos el Blueprint en la aplicación. Todas las rutas definidas
# en chat_bp (como /ask y /ask-image) ahora son parte de la app.
app.register_blueprint(chat_bp)

@app.route('/')
def index():
    return redirect(url_for('chat_bp.ask_model'))









    
# from flask import Flask, jsonify
# import requests

# import base64

# app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World!'


# @app.route("/ask")
# def ask_model():
#     # URL del servidor local de Jan.AI
#     url = "http://127.0.0.1:1337/v1/chat/completions"
    
#     # Cabeceras
#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": "Bearer 12345"
#     }
    
#     # Cuerpo de la petición
#     data = {
#         "model": "gemma-3-4b-it-IQ4_XS",
#         "messages": [
#             {"role": "user", "content": "Tell me a joke."}
#         ]
#     }

#     try:
#         # Hacemos la petición POST
#         response = requests.post(url, headers=headers, json=data)
        
#         # Si responde con éxito
#         if response.status_code == 200:
#             return jsonify(response.json())
#         else:
#             return jsonify({
#                 "error": f"Server responded with {response.status_code}",
#                 "body": response.text
#             }), response.status_code
#     except Exception as e:
#         return jsonify({"error": str(e)}), 500
    
# @app.route("/analyze", methods=["GET"])
# def analyze_image():
    
#     data = {
#         "model": "gemma-3-4b-it-IQ4_XS",
#         "messages": [
#             {
#                 "role": "user",
#                 "content": [
#                     {"type": "text", "text": "Describe this image."},
#                     {
#                         "type": "image_url",
#                         "image_url": {
#                             "url": "https://www.desarrollolibre.net/public/images/course/laravel/laravel.png"
#                         }
#                     }
#                 ]
#             }
#         ]
#     }

#     headers = {
#         "Content-Type": "application/json",
#         "Authorization": "Bearer 12345"
#     }

#     response = requests.post(
#         "http://127.0.0.1:1337/v1/chat/completions",
#         headers=headers,
#         json=data
#     )

#     return jsonify({
#                 "error": f"Server responded with {response.status_code}",
#                 "body": response.text
#             })

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5050)