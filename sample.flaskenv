FLASK_APP=app

# set 1 to debug
FLASK_DEBUG=0

SECRET_KEY='secret-key-goes-here'
SQLALCHEMY_DATABASE_URI='sqlite:///db.sqlite'
SQLALCHEMY_TRACK_MODIFICATIONS=False

#mailtrap credentials
MAIL_SERVER='smtp.mailtrap.io'
MAIL_PORT=2525
MAIL_USERNAME='your-mailtrap-username'
MAIL_PASSWORD='your-mailtrap-password'

MAIL_SENDER='testflaskblog@gmail.com'

#testing credentials
SQLALCHEMY_TEST_DATABASE_URI='sqlite:///test.db'
SERVER_NAME='localhost'
APPLICATION_ROOT='/'