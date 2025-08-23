# src/api/controllers/user_controller.py
from flask import Blueprint, request, jsonify
from api.schemas.user_schema import UserRequestSchema, UserResponseSchema
from infrastructure.services.user_service import UserService

bp = Blueprint('users', __name__, url_prefix='/api')

user_service = UserService()
request_schema = UserRequestSchema()
response_schema = UserResponseSchema()

@bp.route('/users', methods=['POST'])
def create_user():
    """
    Create a new user
    ---
    post:
      summary: Create a new user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/UserRequest'
      responses:
        201:
          description: User created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserResponse'
        400:
          description: Invalid input
    """
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    user = user_service.create_user(data)
    return jsonify(response_schema.dump(user)), 201

@bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Get user by ID
    ---
    get:
      summary: Get a user by ID
      parameters:
        - name: user_id
          in: path
          required: true
          schema:
            type: integer
      responses:
        200:
          description: User info
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/UserResponse'
        404:
          description: User not found
    """
    user = user_service.get_user(user_id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    return jsonify(response_schema.dump(user)), 200

@bp.route('/users', methods=['GET'])
def list_users():
    """
    List all users
    ---
    get:
      summary: List all users
      responses:
        200:
          description: List of users
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/UserResponse'
    """
    users = user_service.list_users()
    return jsonify(response_schema.dump(users, many=True)), 200


