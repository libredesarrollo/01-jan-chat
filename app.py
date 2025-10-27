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
    
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5050)