from flask import Blueprint, request, jsonify
from models import User
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token

bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

@bp.route('/api/register', methods=['POST'])
def register():
    # Logic to handle user registration
    data = request.json
    hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')
    user = User(username=data['username'], password=hashed_password)
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "User registered successfully"}), 201

@bp.route('/api/login', methods=['POST'])
def login():
    # Logic to handle user login
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and bcrypt.check_password_hash(user.password, data['password']):
        token = create_access_token(identity=user.id)
        return jsonify({"token": token}), 200
    return jsonify({"error": "Invalid credentials"}), 401
