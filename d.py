
from flask.ext.sqlalchemy import SQLAlchemy 
from flask.ext.heroku import Heroku 
class Users(db.Model):
	__tablename__="users"

	    id = db.Column(db.Integer, primary_key=True)
	    name = db.Column(db.String(80), unique=True, nullable=False)
	    email = db.Column(db.String(120), unique=True, nullable=False)
        password = db.Column(db.String(20), unique=True, nullable=False)
        sex=db.Column(db.String(1),unique=False,nullable=True)
        age=db.Column(db.String(5),unique=False,nullable=True)

	"""docstring fos users"""
	def __init__(self, name):
		self.name=name

	def __init__(self,email)
	     self.email=email  
    def __init__(self,password):
	     self.password=password
    def __init__(self, sex):
	      self.sex=sex
	def __init__(self, age):
	      	self.age=age
if request.method == 'POST':
        email = request.form['email']
        # Check that email does not already exist (not a great query, but works)
        if not db.session.query(User).filter(User.email == email).count():
            email = User(email)
            db.session.add(email)
            db.session.commit()
            return render_template('signup.html')
    

if __name__ == '__main__':
    #app.debug = True
    app.run()