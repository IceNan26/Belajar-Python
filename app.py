from flask import Flask,render_template,request
app = Flask(__name__)

@app.route('/')

def Helo():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        return 'Selamat Datang di Halaman Profile' + request.form['name']
    return render_template('login.html')

@app.route('/Daftar')
def SignUp():
    return render_template('sign-up.html')
