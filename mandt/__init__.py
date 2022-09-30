from flask import Flask
from flask_mail import Mail

from mandt.main.routes import page_not_found

app = Flask(__name__)
app.register_error_handler(404, page_not_found)

app.secret_key = "edeacda59ac156398eb419c6b1ba496a5b8d0250cbf6f09299"

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'jamesmark7772021@gmail.com'
app.config['MAIL_PASSWORD'] = 'yrvfejyiruzsqqgt'

mail = Mail(app)
from mandt.main.routes import main
from mandt.portals.routes import portals

app.register_blueprint(main)
app.register_blueprint(portals)