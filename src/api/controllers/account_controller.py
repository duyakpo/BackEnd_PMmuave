from flask import Blueprint, request, jsonify
from api.schemas.account_schema import AccountRequestSchema, AccountResponseSchema, AccountRoleUpdateSchema
from infrastructure.services.account_service import AccountService

bp = Blueprint('account', __name__, url_prefix='/api')

account_service = AccountService()
request_schema = AccountRequestSchema()
response_schema = AccountResponseSchema()
role_schema = AccountRoleUpdateSchema()

# ----------------- User APIs -----------------

@bp.route('/auth/register', methods=['POST'])
def register():
    """
    Register a new user
    ---
    post:
      summary: Register a new account
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AccountRequest'
      responses:
        201:
          description: Account created successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AccountResponse'
        400:
          description: Invalid input
    """
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    account = account_service.create_account(data)
    return jsonify(response_schema.dump(account)), 201

@bp.route('/auth/login', methods=['POST'])
def login():
    """
    Login user
    ---
    post:
      summary: Login with email and password
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AccountRequest'
      responses:
        200:
          description: Login successful
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AccountResponse'
        401:
          description: Unauthorized
    """
    data = request.get_json()
    account = account_service.login(data)
    if not account:
        return jsonify({"message": "Unauthorized"}), 401
    return jsonify(response_schema.dump(account)), 200
@bp.route('/me', methods=['GET'])
def get_me():
    """
    Get current user info
    ---
    get:
      summary: Get info of the currently logged-in user
      responses:
        200:
          description: Current user info
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AccountResponse'
        404:
          description: User not found
    """
    # Lấy thông tin user từ header "X-MA-USER" tạm thời (thay JWT)
    ma_user = request.headers.get("X-MA-USER")
    if not ma_user:
        return jsonify({"message": "User not specified"}), 400
    account = account_service.get_me(ma_user)
    if not account:
        return jsonify({"message": "User not found"}), 404
    return jsonify(response_schema.dump(account)), 200


@bp.route('/me', methods=['PUT'])
def update_me():
    """
    Update current user info
    ---
    put:
      summary: Update info of the currently logged-in user
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AccountRequest'
      responses:
        200:
          description: User updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AccountResponse'
        404:
          description: User not found
    """
    ma_user = request.headers.get("X-MA-USER")
    if not ma_user:
        return jsonify({"message": "User not specified"}), 400
    data = request.get_json()
    account = account_service.update_me(ma_user, data)
    if not account:
        return jsonify({"message": "User not found"}), 404
    return jsonify(response_schema.dump(account)), 200

    """
    Update current user info
    ---
    put:
      summary: Update user info by ma_user
      parameters:
        - name: ma_user
          in: query
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AccountRequest'
      responses:
        200:
          description: User updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AccountResponse'
        404:
          description: User not found
    """
    ma_user = request.args.get("ma_user")
    if not ma_user:
        return jsonify({"message": "ma_user is required"}), 400
    data = request.get_json()
    account = account_service.update_me(ma_user, data)
    if not account:
        return jsonify({"message": "User not found"}), 404
    return jsonify(response_schema.dump(account)), 200

# ----------------- Admin / Operator APIs -----------------

@bp.route('/users', methods=['GET'])
def get_all_users():
    """
    Get all users (Admin/Operator)
    ---
    get:
      summary: List all users
      responses:
        200:
          description: List of all users
          content:
            application/json:
              schema:
                type: array
                items:
                  $ref: '#/components/schemas/AccountResponse'
    """
    users = account_service.list_users()
    return jsonify(response_schema.dump(users, many=True)), 200

@bp.route('/users', methods=['POST'])
def create_user_by_admin():
    """
    Create user (Admin/Operator)
    ---
    post:
      summary: Create a user as Admin/Operator
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AccountRequest'
      responses:
        201:
          description: User created
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AccountResponse'
        400:
          description: Invalid input
    """
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    account = account_service.create_account(data)
    return jsonify(response_schema.dump(account)), 201

@bp.route('/users/<string:ma_user>/role', methods=['PUT'])
def update_user_role(ma_user):
    """
    Update user role (Admin/Operator)
    ---
    put:
      summary: Update role of a user by ma_user
      parameters:
        - name: ma_user
          in: path
          required: true
          schema:
            type: string
      requestBody:
        required: true
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AccountRoleUpdate'
      responses:
        200:
          description: Role updated successfully
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AccountResponse'
        404:
          description: User not found
    """
    data = request.get_json()
    errors = role_schema.validate(data)
    if errors:
        return jsonify(errors), 400
    account = account_service.update_role(ma_user, data.get("vai_tro"))
    if not account:
        return jsonify({"message": "User not found"}), 404
    return jsonify(response_schema.dump(account)), 200

