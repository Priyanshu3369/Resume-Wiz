from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from app import mongo
from bson.objectid import ObjectId

resume_bp = Blueprint('resume', __name__)

@resume_bp.route('/', methods=['GET'])
@jwt_required()
def get_resume():
    user_id = get_jwt_identity()
    resume = mongo.db.resumes.find_one({'user_id': ObjectId(user_id)})
    if resume:
        resume['_id'] = str(resume['_id'])
        return jsonify(resume), 200
    return jsonify({'sections': {}}), 200

@resume_bp.route('/', methods=['POST'])
@jwt_required()
def save_resume():
    user_id = get_jwt_identity()
    data = request.json

    mongo.db.resumes.update_one(
        {'user_id': ObjectId(user_id)},
        {'$set': {'sections': data.get('sections', {})}},
        upsert=True
    )
    return jsonify({'msg': 'Resume saved'}), 200
