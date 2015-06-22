from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	#Creating fake user
	user = {'nickname':'Rahul'}
	#Creating fake posts for fake user
	posts = [
			{'author':{'nickname':'King'},
			 'body':'Awesome Weather In Bengaluru!'},
			{'author':{'nickname':'Queen'},
			 'body':'Where is my King!'}
			]
	return render_template('index.html',title='Home',user=user,posts=posts)