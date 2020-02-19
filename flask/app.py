from flask import Flask as fl
from flask import render_template,escape,request
from flask_sqlalchemy import SQLAlchemy as sql
from datetime import datetime

app = fl(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'

db = sql(app)

class database(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    title = db.Column(db.String(50),nullable=False)
    konten = db.Column(db.Text,nullable=False)
    pengarang = db.Column(db.String,nullable=False,default='N/A')
    tanggal = db.Column(db.DateTime,nullable=False,default=datetime.utcnow)

    def __repr__(self):
        return 'Post ke ' + str(self.id)

semua_posts = [
    {
        'judul'     : 'Post1',
        'konten'    : 'Roses are red Violet is blue i want to go to the bathroom',
        'pengarang' : 'Pattrick Star'
    },
    {
        'judul'     : 'Post2',
        'konten'    : 'I wanna poop '
    }
]
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html',data = semua_posts )

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html',user=username)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return 'Mantaap bro kamu berhasil login username kamu adalah ' + request.form['username']
    return render_template('login.html')


if __name__ == "__main__" :
    app.run(debug=True)
