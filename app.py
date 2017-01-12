

__author__ = 'alienchang'
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource,Api
from app import app
from app import settings
from app import  database
db  = database.db
api = Api(app)
def configure_app(flask_app):
    flask_app.config['SERVER_NAME']                     = settings.FLASK_SERVER_NAME
    flask_app.config['SQLALCHEMY_DATABASE_URI']         = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS']  = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION']        = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE']               = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER']           = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP']                  = settings.RESTPLUS_ERROR_404_HELP


def initialize_app(flask_app):
    configure_app(flask_app)
    db.init_app(flask_app)

def main():
    initialize_app(app)
    app.run()

class HelloWorld(Resource):
    def get(self):
        return {'hello' :'world'}
api.add_resource(HelloWorld ,'/')


if __name__ == "__main__":
    main()
