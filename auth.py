from flask import Blueprint, request, jsonify
from models import db, User
from flask_jwt_extended import create_access_token, create_refresh_token, jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "User already exists"}), 400

    user = User(email=data['email'], role=data.get('role', 'customer'))
    user.set_password(data['password'])

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(email=data['email']).first()

    if not user or not user.check_password(data['password']):
        return jsonify({"error": "Invalid credentials"}), 401

    access_token = create_access_token(identity={"id": user.id, "role": user.role})
    refresh_token = create_refresh_token(identity={"id": user.id, "role": user.role})

    return jsonify({"access_token": access_token, "refresh_token": refresh_token}), 200

@auth_bp.route('/logout', methods=['GET'])
@jwt_required()
def logout():
    return jsonify({"message": "Logged out successfully"}), 200
