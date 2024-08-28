from flask import Blueprint, jsonify
from models import User, Data
from flask_jwt_extended import jwt_required

bp = Blueprint('admin', __name__)

@bp.route('/api/admin/users', methods=['GET'])
@jwt_required()
def manage_users():
    # Logic to fetch and return all users
    users = User.query.all()
    return jsonify([u.to_dict() for u in users]), 200

@bp.route('/api/admin/data', methods=['GET'])
@jwt_required()
def manage_data():
    # Logic to fetch and return all data
    data = Data.query.all()
    return jsonify([d.to_dict() for d in data]), 200
