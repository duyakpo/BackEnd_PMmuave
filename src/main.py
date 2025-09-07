import sys
from pathlib import Path
from flask import Flask

# Thêm thư mục src vào sys.path để Python tìm thấy modules
sys.path.append(str(Path(__file__).parent))

from database import Base, engine
import model   # ở src có file model.py

# Import các blueprint
from controllers.checkin import bp_checkin
from controllers.booth import bp_booth
from controllers.survey import bp_survey
from controllers.response import bp_response


def create_app():
    app = Flask(__name__)

    # Tạo các bảng trong database nếu chưa có
    Base.metadata.create_all(bind=engine)

    # Đăng ký các blueprint
    app.register_blueprint(bp_checkin)
    app.register_blueprint(bp_booth)
    app.register_blueprint(bp_survey)
    app.register_blueprint(bp_response)

    return app


app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
