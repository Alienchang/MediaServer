from flask import Flask ,request
import flask_restful
from flask_restful import Resource,Api
from flaskext.mysql import MySQL
from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql:host=127.0.0.1;dbname=wqj_dev'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:123456@127.0.0.1/wqj_dev'

db = SQLAlchemy(app)
db.init_app(app)
mysql = MySQL()
mysql.init_app(app)
api = Api(app)



class AddressBook(db.Model):
    id = db.Column(db.Integer ,primary_key = True)
    phone = db.Column(db.String() ,nullable = True)
    def __init__(self ,phone):
        self.phone = phone
    def __repr__(self):
        return self.phone



class Test(flask_restful.Resource):
    def get(self):
        db.session.query(AddressBook)
        # SQLAlchemy.create_engine('mysql://root:123456@127.0.0.1/wqj_dev')
        # Session = sessionmaker(bind=create_engine('mysql+pymysql:host=127.0.0.1;dbname=wqj_dev'))
        # session = Session()
        # session.query(AddressBook).first()
        addressBook = db.session.query(AddressBook).first();

        return addressBook.id

api.add_resource(Test ,'/test')

class HelloWorld(flask_restful.Resource):
    def get(self):
        return {'hello' :'world'}

api.add_resource(HelloWorld ,'/')


todos = {}

class TodoSimple(Resource):
    def get(self ,todo_id):
        return {todo_id : todos[todo_id]}
    def put(self ,todo_id):
        todos[todo_id] = request.form['data']
        return {todo_id :todos[todo_id]}

api.add_resource(TodoSimple ,'/<string:todo_id>')


if __name__ == '__main__':
    app.run()
