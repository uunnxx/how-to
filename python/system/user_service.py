from flask import Flask, jsonify, request

app = Flask(__name__)


# Create a dictionary to store the user information
users = {}


# Endpoint to create a new user
@app.route('/users', methods=['POST'])
def create_user():
    # Get the user information from the request body
    data = request.get_json()
    user_id = len(users) + 1
    name = data.get('name')
    email = data.get('email')

    # Store the user information in the users dictionary
    users[user_id] = {
        'id': user_id,
        'name': name,
        'email': email
    }

    return jsonify({'message': 'User created successufully'})


# Endpoint to get a user's information by their id
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = users.get(user_id)

    if user:
        return jsonify(user)
    else:
        return jsonify({'message': 'User not found'}), 404


# Endpointto update a user's information by their id
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    user = users.get(user_id)

    if user:
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')

        user['name'] = name
        user['email'] = email

        return jsonify({'message': 'User updated successufully!'})
    else:
        return jsonify({'message': 'User not found'}), 404


# Endpoint to delete a user by their id
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = users.get(user_id)

    if user:
        del users[user_id]
        return jsonify({'message': 'User deleted successufully!'})
    else:
        return jsonify({'message': 'User not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
