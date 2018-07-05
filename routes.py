from flask import Flask ,render_template
from userdef import *
from cvdef import *
app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.sqlite3'
@app.route('/')
def hello_world():
    return render_template('layout.html')
@app.route('/login')
def login():
    return render_template('home.html')
@app.route('/logout')
def logout():
    return render_template('layout.html')
@app.route('/register')
def register():
    return render_template('layout.html')

if __name__ == '__main__':
 app.run(debug=True)
