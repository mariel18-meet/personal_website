from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os
# from flask_heroku import Heroku 

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# heroku = Heroku(app)
db=SQLAlchemy(app)

class Users(db.Model):
	__tablename__="users"
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(20), unique=True, nullable=False)
	sex=db.Column(db.String(1),unique=False,nullable=True)
	age=db.Column(db.String(5),unique=False,nullable=True)

	def __init__(self, name, email, password, sex, age ):
		self.name=name
		self.email=email  
		self.password=password
		self.sex=sex
		self.age=age
db.create_all()

class Posts(db.Model):
	__tablename__="posts"
	id = db.Column(db.Integer, primary_key=True)
	problem= db.Column(db.String(500), unique=False, nullable=False)
	name = db.Column(db.String(30), unique=False, nullable=False)
	Description = db.Column(db.String(1000), unique=False, nullable=False)
	
	def __init__(self, problem, name, Description ):
		self.problem=problem
		self.name=name  
		self.Description=Description
		
		
db.create_all()


@app.route("/")
@app.route("/home",methods= ['GET' , 'POST'])
def home():
	if request.method=='GET':
		return render_template("home.html")
	else:
		name=request.form['name']
		problem=request.form['form']
		Description=request.form["Description"]


	return render_template('home.html', posts = posts, problem=post.problem , name=post.name, Description=post.Description)


@app.route("/add")
def add():
	return render_template('add.html')


@app.route("/signin", methods= ['GET' , 'POST'])
def signin():
	if request.method== 'GET':
		return render_template('signin.html')
	else:
		email=request.form ['email']
		user=Users.query.filter_by(email=email).first()
		password=request.form['password']
		if user.password==password :
			return render_template('home.html',name=user.name , email= user.email , age=user.age , id=user.id   ) 





@app.route("/signup" )
def signup():
	 return render_template('signup.html')

@app.route("/createuser" ,methods=['POST'] )
def createuser():
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

@app.route("/posts", methods=['POST'])
def posts():
	data=request.data
	problem=request.form['problem']
	name=request.form['name']
	Description=request.form['Description']
	post=Posts(problem,name,Description)
	db.session.add(post)
	db.session.commit()
	'''pl=posts.query.all()'''

	return render_template('home.html', problem=post.problem , name=post.name, Description=post.Description)

	
	 # if request.method == 'POST':
	 #         email = request.form['email']
	 #         # Check that email does not already exist (not a great query, but works)
	 #         if not db.session.query(User).filter(User.email == email).count():
	 #             email = User(email)
	 #             db.session.add(email)
	 #             db.session.commit()
	 #             return render_template('signup.html')
'''
@app.route("/login", methods=[ 'GET' , 'POST'] )
def login():
	if request.method == 'POST':
	   email = request.form['email'] 
	   user = Users.session.query(email = email).first()

	if request.form['password'] == user.password:
	   session['logged_in'] = True
	   return profile(user.id)

	else:
			flash('wrong password!')
 

@app.route("/profile/<user_id>"):
def profile(user_id):
	posts = 
'''
# app.run()

