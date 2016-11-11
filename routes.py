import os
from flask import Flask, render_template
from forms import signupForm

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']= 'postgress://localhost/nearyou'

app.secret_key = "development-key"

@app.route('/')
def index():
    return render_template('index.html')
    
@app.route('/about')
def about():
    return render_template('about.html')
    
@app.route('/signup')
def signup():
    form = signupForm()
    return render_template('signup.html', form=form)
    
#still in development, this is development port and ip for cloud9 workspace   
if __name__=="__main__":   
    app.run(debug= True,host=os.getenv('IP', '0.0.0.0'),port=int(os.getenv('PORT', 8080)))

