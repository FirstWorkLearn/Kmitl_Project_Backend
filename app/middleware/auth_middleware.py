from flask_jwt_extended import jwt_required, get_jwt_identity
from functools import wraps
from flask import request, jsonify
from app.models.account import Account

def auth_required(role=None):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            jwt_token = request.headers.get('Authorization', None)
            if not jwt_token:
                return jsonify({"message": "Token is missing!"}), 403
            try:
                user_id = get_jwt_identity()
                user = Account.query.get(user_id)
                if not user:
                    return jsonify({"message": "User not found!"}), 403
                if role and user.role != role:
                    return jsonify({"message": "Unauthorized access!"}), 403
            except Exception as e:
                return jsonify({"message": "Token is invalid!"}), 403
            
            return fn(*args, **kwargs)
        return decorator
    return wrapper
