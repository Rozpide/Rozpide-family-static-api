"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Miembros iniciales de la familia
initial_members = [
    {"first_name": "John", "age": 33, "lucky_numbers": [7, 13, 22], "id": 3439},
    {"first_name": "Jane", "age": 35, "lucky_numbers": [10, 14, 3], "id": 3440},
    {"first_name": "Jimmy", "age": 5, "lucky_numbers": [1], "id": 3441},
   
    
]

for member in initial_members:
    jackson_family.add_member(member)

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

# Endpoint para obtener todos los miembros de la familia
@app.route('/members', methods=['GET'])
def get_all_members():
    members = jackson_family.get_all_members()
    return jsonify(members), 200

# Endpoint para obtener un miembro específico de la familia
@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):
    member = jackson_family.get_member(id)
    if member:
        return jsonify(member), 200
    else:
        return jsonify({"error": "Member not found"}), 404

# Endpoint para añadir un nuevo miembro a la familia
@app.route('/member', methods=['POST'])
def add_member():
    member = request.get_json()
    jackson_family.add_member(member)
    return jsonify(member), 200  # Asegúrate de devolver un estado 200

# Endpoint para actualizar un miembro de la familia
@app.route('/member/<int:id>', methods=['PUT'])
def update_member(id):
    data = request.get_json()
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    member = jackson_family.update_member(id, data)
    if member:
        return jsonify({"message": "Member updated successfully"}), 200
    else:
        return jsonify({"error": "Member not found"}), 404

# Endpoint para eliminar un miembro de la familia
@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):
    member = jackson_family.get_member(id)
    if member:
        jackson_family.delete_member(id)
        return jsonify({"done": True}), 200
    else:
        return jsonify({"error": "Member not found"}), 404

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
