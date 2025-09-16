from src.database import Base, engine
import src.model

from src.controllers.checkin import bp_checkin # pyright: ignore[reportMissingImports]
from src.controllers.booth import bp_booth # pyright: ignore[reportMissingImports]
from src.controllers.survey import bp_survey # pyright: ignore[reportMissingImports]
from src.controllers.response import bp_response # pyright: ignore[reportMissingImports]

def Flask(*args, **kwargs):
    raise NotImplementedError

def create_app():
    app = Flask(__name__)

    # Tạo các bảng trong database nếu chưa có
    Base.metadata.create_all(bind=engine)

    # Đăng ký các blueprint
    app.register_blueprint(bp_checkin)
    app.register_blueprint(bp_booth)
    app.register_blueprint(bp_survey)
