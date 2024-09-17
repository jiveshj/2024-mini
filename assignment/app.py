from flask import Flask,session, render_template, redirect,request
import pyrebase

app = Flask(__name__)

config = {
  'apiKey': "AIzaSyDSfGMO0UbvSRRcCq0SgVQ82493k5_G1iM",

  'authDomain': "senior-design-a96f3.firebaseapp.com",

  'projectId': "senior-design-a96f3",

  'storageBucket': "senior-design-a96f3.appspot.com",

  'messagingSenderId': "587480364157",

  'appId': "1:587480364157:web:0c7c11417e2be165a0ad14",

  'measurementId': "G-04TQJ3RHYV",
  'databaseURL':''
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

app.secret_key = 'senior'

@app.route('/',methods = ['POST','GET'])
def index():
    if( 'user' in session):
        return 'Hi,{}'.format(session['user'])
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        try:
            user=auth.sign_in_with_email_and_password(email,password)
            session['user'] = email
        except:
            return 'Failed to login' 
    return render_template('home.html')
@app.route('/logout')
def logout():
    session.pop('user')
    return redirect('/')

if __name__ == '__main___':
    app.run(port = 1111)