from flask import Flask
from database import Base, engine
import models  

from controllers.checkin import bp_checkin
from controllers.booth import bp_booth
from controllers.survey import bp_survey
from controllers.response import bp_response

def create_app():
    app = Flask(__name__)

    Base.metadata.create_all(bind=engine)

    app.register_blueprint(bp_checkin)
    app.register_blueprint(bp_booth)
    app.register_blueprint(bp_survey)
    app.register_blueprint(bp_response)

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)
