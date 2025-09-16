from flask import Blueprint, request, jsonify
from api.schemas.account_schema import (
    AccountRequestSchema,
    AccountResponseSchema,
    AccountRoleUpdateSchema
)
from infrastructure.services.account_service import AccountService

bp = Blueprint("account", __name__, url_prefix="/api")

account_service = AccountService()
request_schema = AccountRequestSchema()
response_schema = AccountResponseSchema()
role_schema = AccountRoleUpdateSchema()


# ----------------- User APIs -----------------

@bp.route("/auth/register", methods=["POST"])
def register():
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify({"success": False, "errors": errors}), 400

    try:
        account = account_service.create_account(data)
        return jsonify({
            "success": True,
            "message": "Account created successfully",
            "data": response_schema.dump(account)
        }), 201
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500


@bp.route("/auth/login", methods=["POST"])
def login():
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify({"success": False, "errors": errors}), 400

    account = account_service.login(data)
    if not account:
        return jsonify({"success": False, "message": "Unauthorized"}), 401

    return jsonify({
        "success": True,
        "message": "Login successful",
        "data": response_schema.dump(account)
    }), 200


@bp.route("/me", methods=["GET"])
def get_me():
    ma_user = request.headers.get("X-MA-USER")
    if not ma_user:
        return jsonify({"success": False, "message": "User not specified"}), 400

    account = account_service.get_me(ma_user)
    if not account:
        return jsonify({"success": False, "message": "User not found"}), 404

    return jsonify({"success": True, "data": response_schema.dump(account)}), 200


@bp.route("/me", methods=["PUT"])
def update_me():
    ma_user = request.headers.get("X-MA-USER")
    if not ma_user:
        return jsonify({"success": False, "message": "User not specified"}), 400

    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify({"success": False, "errors": errors}), 400

    account = account_service.update_me(ma_user, data)
    if not account:
        return jsonify({"success": False, "message": "User not found"}), 404

    return jsonify({
        "success": True,
        "message": "User updated successfully",
        "data": response_schema.dump(account)
    }), 200


# ----------------- Admin / Operator APIs -----------------

@bp.route("/users", methods=["GET"])
def get_all_users():
    users = account_service.list_users()
    return jsonify({
        "success": True,
        "data": response_schema.dump(users, many=True)
    }), 200


@bp.route("/users", methods=["POST"])
def create_user_by_admin():
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return jsonify({"success": False, "errors": errors}), 400

    account = account_service.create_account(data)
    return jsonify({
        "success": True,
        "message": "User created successfully",
        "data": response_schema.dump(account)
    }), 201


@bp.route("/users/<string:ma_user>/role", methods=["PUT"])
def update_user_role(ma_user):
    data = request.get_json()
    errors = role_schema.validate(data)
    if errors:
        return jsonify({"success": False, "errors": errors}), 400

    account = account_service.update_role(ma_user, data.get("vai_tro"))
    if not account:
        return jsonify({"success": False, "message": "User not found"}), 404

    return jsonify({
        "success": True,
        "message": "Role updated successfully",
        "data": response_schema.dump(account)
    }), 200
