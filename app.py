from flask import Flask
from flask import j
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://slava:123456789@127.0.0.1:5432/vk_music_test'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    second_name = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Quizes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    level = db.Column(db.String(80), nullable=False)
    count = db.Column(db.Integer, nullable=False)


@app.route('/hi')
def hello_world():  # put application's code here
    admin = User(username='admin',second_name='admin1', email='admin@example.com')
    db.session.add(admin)
    db.session.commit()
    return 'hi'

@app.route('/user')
def get_users():  # put application's code here 
    users = User.query.all()
    res = [] 
    for user in users: 
        res.append({ 
            'id': user.id, 
            'username':user.username,
            'second_name':user.second_name, 
            'email': user.email
        }) 
    print("\nResponse:") 
    print(res)
    print('\n')
    return jsonify(res)




if __name__ == '__main__':
    app.run()
