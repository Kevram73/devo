from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

login_manager = LoginManager()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root@localhost/resto'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['SECRET_KEY'] = 'resto_key'
db = SQLAlchemy(app)
login_manager.init_app(app)
app.app_context().push()


from service import routes
