from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = 'thisissecret'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:regards@localhost:5432/Boop'


db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(30))
    l_name = db.Column(db.String(30))
    public_id = db.Column(db.String(30), unique=True)
    password = db.Column(db.String(30))
    admin = db.Column(db.Boolean)


class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(50))
    complete = db.Column(db.Boolean)
    user_id = db.Column(db.Integer)


db.create_all()


@app.route('/user', methods=['GET'])
def get_all_users():
    return ''



if __name__ == '__main__':
    app.run(debug=True)
