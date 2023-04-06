from flask import Blueprint, request
from bson import json_util
import json
from app.config import db

user_bp = Blueprint('user', __name__, url_prefix='/api/users')

def check_user_exists(user_id):
    result = db['accounts'].find_one({'id': user_id})
    if result:
        return True
    else:
        return False
    

def get_user_account_secret(user_id):
    result = db['accounts'].find_one({'id': user_id})
    result['_id'] = str(result['_id'])
    return result


@user_bp.route('/<user_id>', methods=['DELETE'])
def logout(user_id):
    db.accounts.delete_one({'id': user_id})
    db.users.delete_one({'user.detail.id': user_id})
    db.courses.delete_one({'id': user_id})
    return str(user_id)
    

@user_bp.route('/', methods=['GET'])
def getUser():
    cursor = db.users.find()
    python_list = list(json.loads(json_util.dumps(doc, default=json_util.default)) for doc in cursor)
    return python_list