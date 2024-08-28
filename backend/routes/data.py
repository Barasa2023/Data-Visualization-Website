from flask import Blueprint, request, jsonify
from models import Data

bp = Blueprint('data', __name__)

@bp.route('/api/upload', methods=['POST'])
def upload_data():
    # Logic to handle file upload
    file = request.files['file']
    if file:
        # Process and save the file
        return jsonify({"message": "File uploaded successfully"}), 201
    return jsonify({"error": "No file provided"}), 400

@bp.route('/api/data', methods=['GET'])
def get_data():
    # Logic to retrieve and return data
    data = Data.query.all()
    return jsonify([d.to_dict() for d in data]), 200

@bp.route('/api/data/<int:id>', methods=['DELETE'])
def delete_data(id):
    # Logic to delete a specific data entry
    data = Data.query.get_or_404(id)
    db.session.delete(data)
    db.session.commit()
    return jsonify({"message": "Data deleted successfully"}), 200