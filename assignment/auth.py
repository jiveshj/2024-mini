import pyrebase
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
email = 'test@gmail.com'
password = 'jiveshj'

#user = auth.create_user_with_email_and_password(email,password)

user = auth.sign_in_with_email_and_password(email,password)
#print(user)
auth.send_password_reset_email(email)
