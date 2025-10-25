from flask import Flask, jsonify
import requests

import base64

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Worldasassa!'


@app.route("/ask")
def ask_model():
    # URL del servidor local de Jan.AI
    url = "http://127.0.0.1:1337/v1/chat/completions"
    
    # Cabeceras
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 12345"
    }
    
    # Cuerpo de la petición
    data = {
        "model": "gemma-3-4b-it-IQ4_XS",
        "messages": [
            {"role": "user", "content": "Tell me a joke."}
        ]
    }

    try:
        # Hacemos la petición POST
        response = requests.post(url, headers=headers, json=data)
        
        # Si responde con éxito
        if response.status_code == 200:
            return jsonify(response.json())
        else:
            return jsonify({
                "error": f"Server responded with {response.status_code}",
                "body": response.text
            }), response.status_code
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@app.route("/analyze", methods=["GET"])
def analyze_image():
    # image_path = request.json.get("path")
    # image_url = "https://cdn.pixabay.com/photo/2025/09/12/15/10/small-copper-9830647_1280.jpg"
    # # image_url = "https://www.desarrollolibre.net/public/images/course/laravel/laravel.webp"
    # # Descargamos la imagen
    # img_data = requests.get(image_url).content
    # img_b64 = base64.b64encode(img_data).decode("utf-8")
    # data_uri = f"data:image/webp;base64,{img_b64}"
    
    # # Leer imagen local y convertir a base64
    # # with open(image_path, "rb") as f:
    # #     image_b64 = base64.b64encode(f.read()).decode("utf-8")
    
    # data = {
    #     "model": "gemma-3-4b-it-IQ4_XS", # solo texto
    #     "messages": [
    #         {
    #             "role": "user",
    #             "content": [
    #                 {"type": "text", "text": "Describe this image."},
    #                 # {"type": "image_url", "image_url": f"data:image/png;base64,{image_b64}"}
    #                 # {"type": "image_url", "image_url": "https://www.desarrollolibre.net/public/images/course/laravel/laravel.webp"}
    #                  {"type": "image_url", "image_url": data_uri}
    #             ]
    #         }
    #     ]
    # }

    data = {
        "model": "gemma-3-4b-it-IQ4_XS",
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": "Describe this image."},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": "https://cdn.pixabay.com/photo/2025/09/12/15/10/small-copper-9830647_1280.jpg"
                        }
                    }
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 12345"
    }

    response = requests.post(
        "http://127.0.0.1:1337/v1/chat/completions",
        headers=headers,
        json=data
    )

    return jsonify({
                "error": f"Server responded with {response.status_code}",
                "body": response.text
            })

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5050)