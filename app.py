from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)


class Rank(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(225))
    score = db.Column(db.Integer())


    @property
    def serialize(self):
        return {
            'username': self.username,
            'score': self.score
        }


    def __repr__(self):
        return 'Rank[{0}]'.format(self.username)


@app.route('/')
def index():
    return 'Index'


@app.route('/add')
def add_rank():
    username = request.args.get('username', None)
    score = request.args.get('score', 0)
    if username and score:
        rank = Rank(username=username, score=int(score))
        db.session.add(rank)
        db.session.commit()
        return jsonify(msg=1, data='add success')
    return jsonify(msg=0)


@app.route('/ranks')
def show_rank():
    ranks = Rank.query.order_by(Rank.score.desc()).limit(10)
    data = [item.serialize for item in ranks]
    return jsonify(msg=1, data=data)



if __name__ == '__main__':
    app.run()
