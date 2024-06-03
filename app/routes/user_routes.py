from flask import Blueprint, jsonify

user_bp = Blueprint('user', __name__, url_prefix='/api/v1/user')

#  get all users
@user_bp.route("/all/users",methods=['GET'])

def get_users():
    # Logic to fetch users from the database
    users = [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'},
        {'id': 3, 'name': 'Charlie'}
    ]
    return jsonify(users)

# get single user by id

@user_bp.route("/<int:user_id>",methods=["GET"])

def get_user(user_id):
        # Logic to fetch a user by ID from the database
    user = {'id': user_id, 'name': 'User'}
    return jsonify(user)


