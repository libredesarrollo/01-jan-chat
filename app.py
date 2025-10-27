from flask import Flask, jsonify, request, render_template
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Ahora renderiza el archivo form.html desde la carpeta /templates
    return render_template('form.html')
    
@app.route("/ask", methods=['GET', 'POST'])
def ask_model():
    if request.method == 'GET':
        return "Por favor, usa el formulario en la página de inicio para hacer una pregunta."

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 12345"
    }
    
    # Obtenemos el prompt del cuerpo JSON de la petición
    prompt = request.json.get("prompt", "Tell me a joke.")

    # Cuerpo de la petición
    data = {
        "model": "gemma-3-12b-it-IQ4_XS",
        "messages": [
            #   {"role": "user", "content": request.form.get("prompt", "Tell me a joke.")}
            {"role": "user", "content": prompt}
        ]
    }

    try:
        # URL del servidor local de Jan.AI
        url = "http://127.0.0.1:1337/v1/chat/completions"

        # Hacemos la petición POST
        response = requests.post(url, headers=headers, json=data, stream=False) # stream=False para respuestas completas
        
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
    
@app.route("/ask-image", methods=["GET"])
def ask_model_image():
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