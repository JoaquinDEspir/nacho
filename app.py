from flask import Flask, request, jsonify, send_file
import os
import shutil

app = Flask(__name__)

# Directorios de destino
folders = {
    '1': r'C:\Users\joaqu\Desktop\mj soft\Nacho\1',
    '2': r'C:\Users\joaqu\Desktop\mj soft\Nacho\2',
    '3': r'C:\Users\joaqu\Desktop\mj soft\Nacho\3',
    '4': r'C:\Users\joaqu\Desktop\mj soft\Nacho\4',
    '5': r'C:\Users\joaqu\Desktop\mj soft\Nacho\5',
}

@app.route('/')
def index():
    return send_file('static/index.html')

@app.route('/move', methods=['POST'])
def move_file():
    file = request.files['file']
    folder = request.form['folder']

    if folder not in folders:
        return jsonify({'message': 'Carpeta no válida.'}), 400

    # Guardar el archivo temporalmente
    temp_path = os.path.join('uploads', file.filename)
    os.makedirs('uploads', exist_ok=True)
    file.save(temp_path)

    # Mover el archivo a la carpeta seleccionada
    dest_path = os.path.join(folders[folder], file.filename)
    shutil.move(temp_path, dest_path)

    # Verificar que el archivo se haya movido y eliminado del directorio temporal
    if not os.path.exists(temp_path):
        return jsonify({'message': f'Archivo movido a la carpeta {folder} y eliminado de la carpeta temporal.'})
    else:
        return jsonify({'message': f'Error al mover el archivo a la carpeta {folder}.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
