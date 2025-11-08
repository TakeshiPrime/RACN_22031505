from flask import Flask, jsonify, render_template, send_from_directory, request

# Se definen las carpetas static y templates
app = Flask(__name__, static_folder='static', template_folder='templates')

# --- RUTA PRINCIPAL ---
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

# --- RUTA API QUE RECIBE UN PARÁMETRO ---
@app.route('/api/hello', methods=['GET'])
def hello():
    # Obtener el parámetro 'nombre' de la URL
    nombre = request.args.get('nombre', 'Invitado')  # Valor por defecto si no se manda nada
    
    # Respuesta en formato JSON (igual que el estilo anterior que te gustó)
    return jsonify({
        "estado": "exitoso",
        "mensaje": f"Hola {nombre}, bienvenido al servidor Flask de Takeshi Prime 🔥",
        "nombre": nombre
    })

# --- RUTA PARA EL FAVICON ---
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(app.static_folder, 'favicon.ico')

# --- EJECUCIÓN DEL SERVIDOR ---
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
