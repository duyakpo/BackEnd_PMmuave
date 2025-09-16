# run.py
from ticketing_app import create_app, db

app = create_app()

# Tạo bảng nếu chưa có
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
