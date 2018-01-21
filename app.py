from flask import Flask
from flask import render_template
from flask.ext.sqlalchemy import SQLAlchemy 
from flask.ext.heroku import Heroku 
from flask import request



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db=SQLAlchemy(app)
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/add")
def add():
    return render_template('add.html')


@app.route("/signin")
def signin():
    return render_template('signin.html')


@app.route("/signup")
def signup():
     return render_template('signup.html')

@app.route("/db" , methods=['POST'] )
def db():
	data=request.data
	name=request.form['name']
	email=request.form['email']
	password=request.form['password']
	sex=request.form['sex']
	age=request.form['age']
	user= Users(name, email,password,sex,age)
	db.session.add(user)
	db.session.commit()
	return render_template('signin.html')

db.create_all()
class Users(db.Model):
         __tablename__="users"

     	    id = db.Column(db.Integer, primary_key=True)
     	    name = db.Column(db.String(80), unique=True, nullable=False)
     	    email = db.Column(db.String(120), unique=True, nullable=False)
             password = db.Column(db.String(20), unique=True, nullable=False)
             sex=db.Column(db.String(1),unique=False,nullable=True)
             age=db.Column(db.String(5),unique=False,nullable=True)

     	"""docstring fos users"""
     	def __init__(self, name,email,password.sex,age):
     		self.name=name
     	     self.email=email  
              self.password=password
              self.sex=sex
     	     self.age=age
     # if request.method == 'POST':
     #         email = request.form['email']
     #         # Check that email does not already exist (not a great query, but works)
     #         if not db.session.query(User).filter(User.email == email).count():
     #             email = User(email)
     #             db.session.add(email)
     #             db.session.commit()
     #             return render_template('signup.html')

  