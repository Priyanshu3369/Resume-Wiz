from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from app import mongo
from bson.objectid import ObjectId

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.json
    users = mongo.db.users

    if users.find_one({'email': data['email']}):
        return jsonify({'msg': 'User already exists'}), 400

    hashed_password = generate_password_hash(data['password'])
    users.insert_one({'email': data['email'], 'password': hashed_password})
    return jsonify({'msg': 'User registered successfully'}), 201

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = mongo.db.users.find_one({'email': data['email']})

    if not user or not check_password_hash(user['password'], data['password']):
        return jsonify({'msg': 'Invalid credentials'}), 401

    access_token = create_access_token(identity=str(user['_id']))
    return jsonify({'access_token': access_token}), 200


@auth_bp.route('/me', methods=['GET'])
@jwt_required()
def me():
    user_id = get_jwt_identity()
    user = mongo.db.users.find_one({'_id': ObjectId(user_id)})

    if not user:
        return jsonify({'msg': 'User not found'}), 404

    # Convert ObjectId to string to return in JSON
    user['_id'] = str(user['_id'])
    return jsonify(user), 200