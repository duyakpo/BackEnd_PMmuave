<<<<<<< HEAD
import models
from controllers.checkin import bp_checkin

=======
import sys
from pathlib import Path
from flask import Flask
>>>>>>> master

# Thêm thư mục src vào sys.path để Python tìm thấy modules
sys.path.append(str(Path(__file__).parent))

<<<<<<< HEAD
from flask import Flask
from database import Base, engine
import model  # sửa từ models -> model, vì file của bạn là model.py

=======
from database import Base, engine
import model   # ở src có file model.py

# Import các blueprint
>>>>>>> master
from controllers.checkin import bp_checkin
from controllers.booth import bp_booth
from controllers.survey import bp_survey
from controllers.response import bp_response

<<<<<<< HEAD
=======

>>>>>>> master
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

<<<<<<< HEAD
app = create_app()

if __name__ == "__main__":
    # Chạy app
=======

app = create_app()

if __name__ == "__main__":
>>>>>>> master
    app.run(debug=True)
