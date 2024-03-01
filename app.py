from flask import Flask, jsonify, request
from data_access import UserDAO
from models import User

app = Flask(__name__)
user_dao = UserDAO()

@app.route('/users', methods=['GET'])
def get_users():
    users = user_dao.get_all_users()
    return jsonify([user.serialize() for user in users])

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    required_fields = ['firstName', 'lastName', 'birthYear', 'group']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    user = User(data['firstName'], data['lastName'], data['birthYear'], data['group'])
    user_id = user_dao.add_user(user)
    return jsonify({"id": user_id}), 201

@app.route('/users/<int:id>', methods=['GET'])
def get_user(id):
    user = user_dao.get_user_by_id(id)
    if user:
        return jsonify(user.serialize())
    else:
        return jsonify({"error": "User not found"}), 404

@app.route('/users/<int:id>', methods=['PATCH'])
def update_user(id):
    user = user_dao.get_user_by_id(id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400

    if 'firstName' in data:
        user.first_name = data['firstName']
    if 'lastName' in data:
        user.last_name = data['lastName']
    if 'birthYear' in data:
        user.birth_year = data['birthYear']
    if 'group' in data:
        user.group = data['group']

    user_dao.update_user(user)
    return jsonify({"message": "User updated successfully"}), 200

@app.route('/users/<int:id>', methods=['DELETE'])
def delete_user(id):
    user = user_dao.get_user_by_id(id)
    if not user:
        return jsonify({"error": "User not found"}), 404

    user_dao.delete_user(id)
    return jsonify({"message": "User deleted successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
