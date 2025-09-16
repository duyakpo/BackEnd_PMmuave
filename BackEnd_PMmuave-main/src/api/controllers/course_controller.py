from flask import Blueprint, request, jsonify
from services.todo_service import TodoService
from infrastructure.repositories.todo_repository import TodoRepository
from api.schemas.todo import TodoRequestSchema, TodoResponseSchema
from datetime import datetime

bp = Blueprint('todo', __name__, url_prefix='/todos')

# Khởi tạo service và repository (dùng memory, chưa kết nối DB thật)
todo_service = TodoService(TodoRepository())

request_schema = TodoRequestSchema()
response_schema = TodoResponseSchema()

# Helpers
def success_response(data=None, message="OK", status=200):
    return jsonify({"success": True, "message": message, "data": data}), status

def error_response(message, status=400):
    return jsonify({"success": False, "message": message}), status


@bp.route('/', methods=['GET'])
def list_todos():
    """Get all todos"""
    todos = todo_service.list_todos()
    return success_response(response_schema.dump(todos, many=True), "Danh sách todos")


@bp.route('/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = todo_service.get_todo(todo_id)
    if not todo:
        return error_response("Todo not found", 404)
    return success_response(response_schema.dump(todo), "Chi tiết todo")


@bp.route('/', methods=['POST'])
def create_todo():
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return error_response(errors, 400)

    now = datetime.utcnow()
    todo = todo_service.create_todo(
        title=data['title'],
        description=data['description'],
        status=data['status'],
        created_at=now,
        updated_at=now
    )
    return success_response(response_schema.dump(todo), "Tạo todo thành công", 201)


@bp.route('/<int:todo_id>', methods=['PUT'])
def update_todo(todo_id):
    data = request.get_json()
    errors = request_schema.validate(data)
    if errors:
        return error_response(errors, 400)

    todo = todo_service.update_todo(
        todo_id=todo_id,
        title=data['title'],
        description=data['description'],
        status=data['status'],
        updated_at=datetime.utcnow()
    )
    if not todo:
        return error_response("Todo not found", 404)

    return success_response(response_schema.dump(todo), "Cập nhật thành công")


@bp.route('/<int:todo_id>', methods=['DELETE'])
def delete_todo(todo_id):
    deleted = todo_service.delete_todo(todo_id)
    if not deleted:
        return error_response("Todo not found", 404)
    return success_response(None, "Xóa todo thành công", 200)
