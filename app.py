from flask import Flask
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from serializers import user_schema, users_schema, quizes_schema, quize_schema

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://slava:123456789@127.0.0.1:5432/vk_music_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


# from models import User, Quizes, Answers, Questions
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=True)
    second_name = db.Column(db.String(80), unique=True, nullable=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    vk_id = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Quizes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    level = db.Column(db.String(80), nullable=False)
    count = db.Column(db.Integer, nullable=True)

    @property
    def questions(self):
        return Questions.query.filter_by(quiz_id=self.id).all()


class Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.id'), nullable=False)
    right = db.Column(db.Boolean, nullable=False)


class Questions(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quizes.id'), nullable=False)
    music_id = db.Column(db.String(80), nullable=False)

    @property
    def answers(self):
        return Answers.query.filter_by(question_id=self.id).all()


@app.route('/user/<string:vk_id>')
def hello_world(vk_id):
    user = User.query.filter_by(vk_id=vk_id).first()
    return jsonify(user_schema.dump(user))


@app.route('/users')
def get_users():
    users = User.query.all()
    return jsonify(users_schema.dump(users))


@app.route('/quizes', methods=['GET'])
def get_quizes():
    quizes = Quizes.query.all()
    return jsonify(quizes_schema.dump(quizes))


@app.route('/quiz/<int:quiz_id>', methods=['GET'])
def get_user(quiz_id):
    quiz = Quizes.query.filter_by(id=quiz_id).first()
    return jsonify(quize_schema.dump(quiz))


if __name__ == '__main__':
    app.run()
